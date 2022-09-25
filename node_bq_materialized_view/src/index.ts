import { BigQuery, RowMetadata, TableField, TableMetadata } from '@google-cloud/bigquery';
import 'dotenv/config';

const extractEnvVar = (key: string) => {
  const value = process.env[key];
  if (value === undefined) {
    throw new Error(`environment variable ${key} doesn't set yet.`);
  }
  return value;
};

const bqClient = new BigQuery({
  projectId: extractEnvVar('GCP_PROJECT_ID'),
  location: extractEnvVar('GCP_LOCATION'),
  scopes: [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/bigquery',
  ],
});

async function createDataset(datasetId: string) {
  const [isDatasetExist] = await bqClient.dataset(datasetId).exists();
  console.log(`isDatasetExist: ${isDatasetExist}`)

  if (!isDatasetExist) {
    const res = await bqClient.createDataset(datasetId);
    console.log(res);
  }
}

async function createTable(datasetId: string, tableId: string, schema: TableField[]) {
  const dataset = bqClient.dataset(datasetId)
  const [isTableExist] = await dataset.table(tableId).exists();
  console.log(`isTableExist: ${isTableExist}`)

  if (!isTableExist) {
    const options: TableMetadata = {
      location: extractEnvVar('GCP_LOCATION'),
      schema: schema,
    };
    const res = await dataset.createTable(tableId, options);
    console.log(res);
  }
}

async function loadDataToTable(datasetId: string, tableId: string, loadData: RowMetadata | RowMetadata[],) {
  const table = bqClient.dataset(datasetId).table(tableId)
  table.insert(loadData, function (err, response) {
    console.log("error:" + JSON.stringify(err));
    console.log("response:" + JSON.stringify(response));
  });
}

async function createMaterializedView(datasetId: string, tableId: string, query: string) {
  const dataset = bqClient.dataset(datasetId)
  const options: TableMetadata = {
    location: extractEnvVar('GCP_LOCATION'),
    materializedView: { query: query },
  };
  const res = await dataset.createTable(tableId, options);
  console.log(res);
}

async function main() {
  const sampleDataset = extractEnvVar('GCP_SAMPLE_DATASET')
  const sampleTable = 'sample_table'
  const schema = [
    { name: 'date', type: 'string' },
    { name: 'item_id', type: 'string' },
    { name: 'quantity', type: 'numeric' },
  ]
  await createDataset(sampleDataset);
  await createTable(sampleDataset, sampleTable, schema);
  console.log('Finish preparing table')


  const loadData = [
    { date: '2022-09-01', item_id: '01', quantity: 1 },
    { date: '2022-09-01', item_id: '20', quantity: 20 },
    { date: '2022-09-02', item_id: '15', quantity: 5 },
  ]
  await loadDataToTable(sampleDataset, sampleTable, loadData);
  console.log('Finish loading')

  const query = `
  SELECT date, SUM(quantity) as quantity
  FROM ${sampleDataset}.${sampleTable}
  GROUP BY date
  `;
  const sampleMaterializedView = 'sample_materialized_view'
  await createMaterializedView(sampleDataset, sampleMaterializedView, query);
}

main()
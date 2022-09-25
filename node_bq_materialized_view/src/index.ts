import { BigQuery } from '@google-cloud/bigquery';
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

async function createTable(datasetId: string, tableId: string) {
  const dataset = bqClient.dataset(datasetId)
  const [isTableExist] = await dataset.table(tableId).exists();
  console.log(`isTableExist: ${isTableExist}`)

  if (!isTableExist) {
    const options = {
      location: extractEnvVar('GCP_LOCATION'),
    };
    const res = await dataset.createTable(tableId, options);
    console.log(res);
  }
}

const sampleDataset = extractEnvVar('GCP_SAMPLE_DATASET')
const sampleTable = 'sample_table'
createDataset(sampleDataset);
createTable(sampleDataset, sampleTable);

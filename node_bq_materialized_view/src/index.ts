import { BigQuery } from '@google-cloud/bigquery';
import 'dotenv/config';

console.log(process.env.GCP_PROJECT_ID)
console.log(process.env.GCP_LOCATION)

const extractEnvVar = (key: string) => {
  const value = process.env[key];
  if (value === undefined) {
    throw new Error(`environment variable ${key} doesn't set yet.`);
  }
  return value;
}

const bqClient = new BigQuery({
  projectId: extractEnvVar('GCP_PROJECT_ID'),
  location: extractEnvVar('GCP_LOCATION'),
  scopes: [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/bigquery',
  ],
});

const sampleDatasetName = extractEnvVar('GCP_SAMPLE_DATASET')
const res = bqClient.createDataset(sampleDatasetName);

console.log(res)
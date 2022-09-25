
## References

* 公式ドキュメントのサンプル
  * [スキーマを使用してテーブルを作成する]( https://cloud.google.com/bigquery/docs/samples/bigquery-create-table?hl=ja )
  * [マテリアライズド ビューの作成]( https://cloud.google.com/bigquery/docs/samples/bigquery-create-materialized-view?hl=ja )
    * Node.jsのサンプルはない
* Node.jsのBQクライアントのメモ
  * `IMaterializedViewDefinition`
    * githubだと [ここ]( https://github.com/googleapis/nodejs-bigquery/blob/7933bfe9a1f706f45077e5ea64591aeebd87b27f/src/types.d.ts#L2454 ) に定義されてる
    * queryとかrefreshに関する定義を書ける
  * `ITable`
    * githubだと [ここ]( https://github.com/googleapis/nodejs-bigquery/blob/389fe04ca227e3b034f24b3c1aaccb446db41269/src/types.d.ts#L3314 ) に定義されてる
    * `materializedView?: IMaterializedViewDefinition;` とかが入ってる
  * `TableMetadata`
    * https://cloud.google.com/nodejs/docs/reference/bigquery/latest/overview#_google_cloud_bigquery_TableMetadata_type
    * `export declare type TableMetadata = bigquery.ITable & { name?: string; , …`
    * ほぼ本体は `ITable`
  * `createTable`
    * https://cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/dataset#_google_cloud_bigquery_Dataset_createTable_member_1_
    * optionsとして `TableMetadata` を入れられる

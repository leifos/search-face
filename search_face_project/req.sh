curl -XGET '40.68.209.241:9200/clueweb12_docs/_search?pretty' -H 'Content-Type: application/json' -d '
{
    "query" : {
        "match": { "body": "clueless" }
    },
    "highlight" : {
        "fields" : {
            "body" : {"type" : "plain"}
        }
    }
}'

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
es = Elasticsearch()
es.indices.create(index=index, ignore=400)
records = []
for data in dataList:
    data["timestamp"] = datetime.now().isoformat()
    #es.index(index=index, doc_type="product", id=data["id"], body=data)
    #print "save: %s - %s"%(source.lower(), data["id"])
    record = {}
    record["_index"] = index
    record["_type"] = "product"
    record["_id"] = data["id"]
    record["_source"] =json.dumps(data)
    records.append(record)
bulk(es, records)

# bigdata
bigdata memo


作者：潘飞
链接：https://www.zhihu.com/question/26340484/answer/50846645
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

目前来看大数据分析的技术主要有以下几个方向：
 类似于Hadoop的MapReduce架构；
 类似于Presto和Spark的内存计算架构；
 类似于Elasticsearch的分布式索引架构；
 类似于Storm之类的分布式实时计算框架；

MR算法是传统的批处理模型，其延迟性较为明显，对于体量较大（数据粒度较细）的数据分析比较适合，比如ETL过程就比较适合于使用MR计算模型（可以通过Hive来使用SQL转化成MR）。

类似于Presto这样的架构（可以使用SQL），更多的是应用在即时分析的领域，因为其最大限度地利用内存来提升计算性能，所以其延迟要比基于MR的Hive要低好几个数量级。同时，也应该注意运算的复杂性，确保有足够的内存支持运算；

Elasticsearch是技术Lucene开发的分布式的索引架构，很多设计借鉴了HDFS的设计，比如分片，复制等概念，其最大的优势在于它的准实时性。其对数据分析的支持仅限于简单的聚合计算，所以有其局限性。其最大的问题就是为了性能，消耗内存比较大，所以要适当地保持数据的规模，确保每个节点的内存不会成为瓶颈。

Storm这种是一种数据流计算框架，其最大的优势就在于它的准实时。作为一个纯粹的数据流计算框架来使用，它的性能没有问题，但是如果要做一些稍微复杂一点的计算，比如JOIN操作，那其性能也会受到极大影响。以上所有的计算模型，都要注意内存的使用，特别是Presto和ES，如果服务器节点开始使用交换区的话，性能会呈指数级下降。


我们使用Elasticsearch存储的文档数量接近50亿（算上1份复制，接近100亿文档），总共10个数据节点和2个元数据节点（48GB内存，8核心CPU，ES使用内存达到70%），每天的文档增量大概是3000W条（速度持续增加中）。目前来看，单个文档的查询效率基本处于实时状态；对于1到2周的数据的聚合统计操作也可以在10秒之内返回结果。


http://www.alluxio.org/

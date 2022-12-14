# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/reporter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metrics_pb2 as opencensus_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2
from . import common_pb2 as src_dot_ray_dot_protobuf_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsrc/ray/protobuf/reporter.proto\x12\x07ray.rpc\x1a)opencensus/proto/metrics/v1/metrics.proto\x1a\x1dsrc/ray/protobuf/common.proto\"H\n\x18GetProfilingStatsRequest\x12\x10\n\x03pid\x18\x01 \x01(\rR\x03pid\x12\x1a\n\x08\x64uration\x18\x02 \x01(\x05R\x08\x64uration\"s\n\x16GetProfilingStatsReply\x12\'\n\x0fprofiling_stats\x18\x01 \x01(\tR\x0eprofilingStats\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr\"S\n\x14ReportMetricsRequest\x12;\n\x0emetrics_points\x18\x01 \x03(\x0b\x32\x14.ray.rpc.MetricPointR\rmetricsPoints\"T\n\x12ReportMetricsReply\x12>\n\x1bmetrcs_description_required\x18\x01 \x01(\x08R\x19metrcsDescriptionRequired\"W\n\x16ReportOCMetricsRequest\x12=\n\x07metrics\x18\x01 \x03(\x0b\x32#.opencensus.proto.metrics.v1.MetricR\x07metrics\"\x16\n\x14ReportOCMetricsReply\"\'\n\x11NodeResourceUsage\x12\x12\n\x04json\x18\x01 \x01(\tR\x04json\"\xa8\x01\n\x10StreamLogRequest\x12\"\n\rlog_file_name\x18\x01 \x01(\tR\x0blogFileName\x12\x1d\n\nkeep_alive\x18\x02 \x01(\x08R\tkeepAlive\x12\x19\n\x05lines\x18\x03 \x01(\x05H\x00R\x05lines\x88\x01\x01\x12\x1f\n\x08interval\x18\x04 \x01(\x02H\x01R\x08interval\x88\x01\x01\x42\x08\n\x06_linesB\x0b\n\t_interval\"$\n\x0eStreamLogReply\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"2\n\x0fListLogsRequest\x12\x1f\n\x0bglob_filter\x18\x01 \x01(\tR\nglobFilter\",\n\rListLogsReply\x12\x1b\n\tlog_files\x18\x01 \x03(\tR\x08logFiles2\x8a\x02\n\x0fReporterService\x12W\n\x11GetProfilingStats\x12!.ray.rpc.GetProfilingStatsRequest\x1a\x1f.ray.rpc.GetProfilingStatsReply\x12K\n\rReportMetrics\x12\x1d.ray.rpc.ReportMetricsRequest\x1a\x1b.ray.rpc.ReportMetricsReply\x12Q\n\x0fReportOCMetrics\x12\x1f.ray.rpc.ReportOCMetricsRequest\x1a\x1d.ray.rpc.ReportOCMetricsReply2\x8d\x01\n\nLogService\x12<\n\x08ListLogs\x12\x18.ray.rpc.ListLogsRequest\x1a\x16.ray.rpc.ListLogsReply\x12\x41\n\tStreamLog\x12\x19.ray.rpc.StreamLogRequest\x1a\x17.ray.rpc.StreamLogReply0\x01\x42\x03\xf8\x01\x01\x62\x06proto3')



_GETPROFILINGSTATSREQUEST = DESCRIPTOR.message_types_by_name['GetProfilingStatsRequest']
_GETPROFILINGSTATSREPLY = DESCRIPTOR.message_types_by_name['GetProfilingStatsReply']
_REPORTMETRICSREQUEST = DESCRIPTOR.message_types_by_name['ReportMetricsRequest']
_REPORTMETRICSREPLY = DESCRIPTOR.message_types_by_name['ReportMetricsReply']
_REPORTOCMETRICSREQUEST = DESCRIPTOR.message_types_by_name['ReportOCMetricsRequest']
_REPORTOCMETRICSREPLY = DESCRIPTOR.message_types_by_name['ReportOCMetricsReply']
_NODERESOURCEUSAGE = DESCRIPTOR.message_types_by_name['NodeResourceUsage']
_STREAMLOGREQUEST = DESCRIPTOR.message_types_by_name['StreamLogRequest']
_STREAMLOGREPLY = DESCRIPTOR.message_types_by_name['StreamLogReply']
_LISTLOGSREQUEST = DESCRIPTOR.message_types_by_name['ListLogsRequest']
_LISTLOGSREPLY = DESCRIPTOR.message_types_by_name['ListLogsReply']
GetProfilingStatsRequest = _reflection.GeneratedProtocolMessageType('GetProfilingStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsRequest)
  })
_sym_db.RegisterMessage(GetProfilingStatsRequest)

GetProfilingStatsReply = _reflection.GeneratedProtocolMessageType('GetProfilingStatsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsReply)
  })
_sym_db.RegisterMessage(GetProfilingStatsReply)

ReportMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsRequest)
  })
_sym_db.RegisterMessage(ReportMetricsRequest)

ReportMetricsReply = _reflection.GeneratedProtocolMessageType('ReportMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsReply)
  })
_sym_db.RegisterMessage(ReportMetricsReply)

ReportOCMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportOCMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsRequest)
  })
_sym_db.RegisterMessage(ReportOCMetricsRequest)

ReportOCMetricsReply = _reflection.GeneratedProtocolMessageType('ReportOCMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsReply)
  })
_sym_db.RegisterMessage(ReportOCMetricsReply)

NodeResourceUsage = _reflection.GeneratedProtocolMessageType('NodeResourceUsage', (_message.Message,), {
  'DESCRIPTOR' : _NODERESOURCEUSAGE,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.NodeResourceUsage)
  })
_sym_db.RegisterMessage(NodeResourceUsage)

StreamLogRequest = _reflection.GeneratedProtocolMessageType('StreamLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogRequest)
  })
_sym_db.RegisterMessage(StreamLogRequest)

StreamLogReply = _reflection.GeneratedProtocolMessageType('StreamLogReply', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogReply)
  })
_sym_db.RegisterMessage(StreamLogReply)

ListLogsRequest = _reflection.GeneratedProtocolMessageType('ListLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsRequest)
  })
_sym_db.RegisterMessage(ListLogsRequest)

ListLogsReply = _reflection.GeneratedProtocolMessageType('ListLogsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsReply)
  })
_sym_db.RegisterMessage(ListLogsReply)

_REPORTERSERVICE = DESCRIPTOR.services_by_name['ReporterService']
_LOGSERVICE = DESCRIPTOR.services_by_name['LogService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _GETPROFILINGSTATSREQUEST._serialized_start=118
  _GETPROFILINGSTATSREQUEST._serialized_end=190
  _GETPROFILINGSTATSREPLY._serialized_start=192
  _GETPROFILINGSTATSREPLY._serialized_end=307
  _REPORTMETRICSREQUEST._serialized_start=309
  _REPORTMETRICSREQUEST._serialized_end=392
  _REPORTMETRICSREPLY._serialized_start=394
  _REPORTMETRICSREPLY._serialized_end=478
  _REPORTOCMETRICSREQUEST._serialized_start=480
  _REPORTOCMETRICSREQUEST._serialized_end=567
  _REPORTOCMETRICSREPLY._serialized_start=569
  _REPORTOCMETRICSREPLY._serialized_end=591
  _NODERESOURCEUSAGE._serialized_start=593
  _NODERESOURCEUSAGE._serialized_end=632
  _STREAMLOGREQUEST._serialized_start=635
  _STREAMLOGREQUEST._serialized_end=803
  _STREAMLOGREPLY._serialized_start=805
  _STREAMLOGREPLY._serialized_end=841
  _LISTLOGSREQUEST._serialized_start=843
  _LISTLOGSREQUEST._serialized_end=893
  _LISTLOGSREPLY._serialized_start=895
  _LISTLOGSREPLY._serialized_end=939
  _REPORTERSERVICE._serialized_start=942
  _REPORTERSERVICE._serialized_end=1208
  _LOGSERVICE._serialized_start=1211
  _LOGSERVICE._serialized_end=1352
# @@protoc_insertion_point(module_scope)

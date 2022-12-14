# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opencensus/proto/metrics/v1/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import resource_pb2 as opencensus_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)opencensus/proto/metrics/v1/metrics.proto\x12\x1bopencensus.proto.metrics.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a+opencensus/proto/resource/v1/resource.proto\"\xf1\x01\n\x06Metric\x12Z\n\x11metric_descriptor\x18\x01 \x01(\x0b\x32-.opencensus.proto.metrics.v1.MetricDescriptorR\x10metricDescriptor\x12G\n\ntimeseries\x18\x02 \x03(\x0b\x32\'.opencensus.proto.metrics.v1.TimeSeriesR\ntimeseries\x12\x42\n\x08resource\x18\x03 \x01(\x0b\x32&.opencensus.proto.resource.v1.ResourceR\x08resource\"\x96\x03\n\x10MetricDescriptor\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04unit\x18\x03 \x01(\tR\x04unit\x12\x46\n\x04type\x18\x04 \x01(\x0e\x32\x32.opencensus.proto.metrics.v1.MetricDescriptor.TypeR\x04type\x12\x44\n\nlabel_keys\x18\x05 \x03(\x0b\x32%.opencensus.proto.metrics.v1.LabelKeyR\tlabelKeys\"\xa9\x01\n\x04Type\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bGAUGE_INT64\x10\x01\x12\x10\n\x0cGAUGE_DOUBLE\x10\x02\x12\x16\n\x12GAUGE_DISTRIBUTION\x10\x03\x12\x14\n\x10\x43UMULATIVE_INT64\x10\x04\x12\x15\n\x11\x43UMULATIVE_DOUBLE\x10\x05\x12\x1b\n\x17\x43UMULATIVE_DISTRIBUTION\x10\x06\x12\x0b\n\x07SUMMARY\x10\x07\">\n\x08LabelKey\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\xd9\x01\n\nTimeSeries\x12\x43\n\x0fstart_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0estartTimestamp\x12J\n\x0clabel_values\x18\x02 \x03(\x0b\x32\'.opencensus.proto.metrics.v1.LabelValueR\x0blabelValues\x12:\n\x06points\x18\x03 \x03(\x0b\x32\".opencensus.proto.metrics.v1.PointR\x06points\"?\n\nLabelValue\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x1b\n\thas_value\x18\x02 \x01(\x08R\x08hasValue\"\xc5\x02\n\x05Point\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12!\n\x0bint64_value\x18\x02 \x01(\x03H\x00R\nint64Value\x12#\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00R\x0b\x64oubleValue\x12_\n\x12\x64istribution_value\x18\x04 \x01(\x0b\x32..opencensus.proto.metrics.v1.DistributionValueH\x00R\x11\x64istributionValue\x12P\n\rsummary_value\x18\x05 \x01(\x0b\x32).opencensus.proto.metrics.v1.SummaryValueH\x00R\x0csummaryValueB\x07\n\x05value\"\xcb\x06\n\x11\x44istributionValue\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\x12\x10\n\x03sum\x18\x02 \x01(\x01R\x03sum\x12\x37\n\x18sum_of_squared_deviation\x18\x03 \x01(\x01R\x15sumOfSquaredDeviation\x12\x63\n\x0e\x62ucket_options\x18\x04 \x01(\x0b\x32<.opencensus.proto.metrics.v1.DistributionValue.BucketOptionsR\rbucketOptions\x12O\n\x07\x62uckets\x18\x05 \x03(\x0b\x32\x35.opencensus.proto.metrics.v1.DistributionValue.BucketR\x07\x62uckets\x1a\xa0\x01\n\rBucketOptions\x12\x63\n\x08\x65xplicit\x18\x01 \x01(\x0b\x32\x45.opencensus.proto.metrics.v1.DistributionValue.BucketOptions.ExplicitH\x00R\x08\x65xplicit\x1a\"\n\x08\x45xplicit\x12\x16\n\x06\x62ounds\x18\x01 \x03(\x01R\x06\x62oundsB\x06\n\x04type\x1as\n\x06\x42ucket\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\x12S\n\x08\x65xemplar\x18\x02 \x01(\x0b\x32\x37.opencensus.proto.metrics.v1.DistributionValue.ExemplarR\x08\x65xemplar\x1a\x86\x02\n\x08\x45xemplar\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value\x12\x38\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\x12j\n\x0b\x61ttachments\x18\x03 \x03(\x0b\x32H.opencensus.proto.metrics.v1.DistributionValue.Exemplar.AttachmentsEntryR\x0b\x61ttachments\x1a>\n\x10\x41ttachmentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xef\x03\n\x0cSummaryValue\x12\x31\n\x05\x63ount\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x05\x63ount\x12.\n\x03sum\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03sum\x12N\n\x08snapshot\x18\x03 \x01(\x0b\x32\x32.opencensus.proto.metrics.v1.SummaryValue.SnapshotR\x08snapshot\x1a\xab\x02\n\x08Snapshot\x12\x31\n\x05\x63ount\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x05\x63ount\x12.\n\x03sum\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03sum\x12q\n\x11percentile_values\x18\x03 \x03(\x0b\x32\x44.opencensus.proto.metrics.v1.SummaryValue.Snapshot.ValueAtPercentileR\x10percentileValues\x1aI\n\x11ValueAtPercentile\x12\x1e\n\npercentile\x18\x01 \x01(\x01R\npercentile\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05valueB\x94\x01\n\x1eio.opencensus.proto.metrics.v1B\x0cMetricsProtoP\x01ZDgithub.com/census-instrumentation/opencensus-proto/gen-go/metrics/v1\xea\x02\x1bOpenCensus.Proto.Metrics.V1b\x06proto3')



_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_METRICDESCRIPTOR = DESCRIPTOR.message_types_by_name['MetricDescriptor']
_LABELKEY = DESCRIPTOR.message_types_by_name['LabelKey']
_TIMESERIES = DESCRIPTOR.message_types_by_name['TimeSeries']
_LABELVALUE = DESCRIPTOR.message_types_by_name['LabelValue']
_POINT = DESCRIPTOR.message_types_by_name['Point']
_DISTRIBUTIONVALUE = DESCRIPTOR.message_types_by_name['DistributionValue']
_DISTRIBUTIONVALUE_BUCKETOPTIONS = _DISTRIBUTIONVALUE.nested_types_by_name['BucketOptions']
_DISTRIBUTIONVALUE_BUCKETOPTIONS_EXPLICIT = _DISTRIBUTIONVALUE_BUCKETOPTIONS.nested_types_by_name['Explicit']
_DISTRIBUTIONVALUE_BUCKET = _DISTRIBUTIONVALUE.nested_types_by_name['Bucket']
_DISTRIBUTIONVALUE_EXEMPLAR = _DISTRIBUTIONVALUE.nested_types_by_name['Exemplar']
_DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY = _DISTRIBUTIONVALUE_EXEMPLAR.nested_types_by_name['AttachmentsEntry']
_SUMMARYVALUE = DESCRIPTOR.message_types_by_name['SummaryValue']
_SUMMARYVALUE_SNAPSHOT = _SUMMARYVALUE.nested_types_by_name['Snapshot']
_SUMMARYVALUE_SNAPSHOT_VALUEATPERCENTILE = _SUMMARYVALUE_SNAPSHOT.nested_types_by_name['ValueAtPercentile']
_METRICDESCRIPTOR_TYPE = _METRICDESCRIPTOR.enum_types_by_name['Type']
Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.Metric)
  })
_sym_db.RegisterMessage(Metric)

MetricDescriptor = _reflection.GeneratedProtocolMessageType('MetricDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _METRICDESCRIPTOR,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.MetricDescriptor)
  })
_sym_db.RegisterMessage(MetricDescriptor)

LabelKey = _reflection.GeneratedProtocolMessageType('LabelKey', (_message.Message,), {
  'DESCRIPTOR' : _LABELKEY,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.LabelKey)
  })
_sym_db.RegisterMessage(LabelKey)

TimeSeries = _reflection.GeneratedProtocolMessageType('TimeSeries', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIES,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.TimeSeries)
  })
_sym_db.RegisterMessage(TimeSeries)

LabelValue = _reflection.GeneratedProtocolMessageType('LabelValue', (_message.Message,), {
  'DESCRIPTOR' : _LABELVALUE,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.LabelValue)
  })
_sym_db.RegisterMessage(LabelValue)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.Point)
  })
_sym_db.RegisterMessage(Point)

DistributionValue = _reflection.GeneratedProtocolMessageType('DistributionValue', (_message.Message,), {

  'BucketOptions' : _reflection.GeneratedProtocolMessageType('BucketOptions', (_message.Message,), {

    'Explicit' : _reflection.GeneratedProtocolMessageType('Explicit', (_message.Message,), {
      'DESCRIPTOR' : _DISTRIBUTIONVALUE_BUCKETOPTIONS_EXPLICIT,
      '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
      # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue.BucketOptions.Explicit)
      })
    ,
    'DESCRIPTOR' : _DISTRIBUTIONVALUE_BUCKETOPTIONS,
    '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue.BucketOptions)
    })
  ,

  'Bucket' : _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), {
    'DESCRIPTOR' : _DISTRIBUTIONVALUE_BUCKET,
    '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue.Bucket)
    })
  ,

  'Exemplar' : _reflection.GeneratedProtocolMessageType('Exemplar', (_message.Message,), {

    'AttachmentsEntry' : _reflection.GeneratedProtocolMessageType('AttachmentsEntry', (_message.Message,), {
      'DESCRIPTOR' : _DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY,
      '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
      # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue.Exemplar.AttachmentsEntry)
      })
    ,
    'DESCRIPTOR' : _DISTRIBUTIONVALUE_EXEMPLAR,
    '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue.Exemplar)
    })
  ,
  'DESCRIPTOR' : _DISTRIBUTIONVALUE,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.DistributionValue)
  })
_sym_db.RegisterMessage(DistributionValue)
_sym_db.RegisterMessage(DistributionValue.BucketOptions)
_sym_db.RegisterMessage(DistributionValue.BucketOptions.Explicit)
_sym_db.RegisterMessage(DistributionValue.Bucket)
_sym_db.RegisterMessage(DistributionValue.Exemplar)
_sym_db.RegisterMessage(DistributionValue.Exemplar.AttachmentsEntry)

SummaryValue = _reflection.GeneratedProtocolMessageType('SummaryValue', (_message.Message,), {

  'Snapshot' : _reflection.GeneratedProtocolMessageType('Snapshot', (_message.Message,), {

    'ValueAtPercentile' : _reflection.GeneratedProtocolMessageType('ValueAtPercentile', (_message.Message,), {
      'DESCRIPTOR' : _SUMMARYVALUE_SNAPSHOT_VALUEATPERCENTILE,
      '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
      # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.SummaryValue.Snapshot.ValueAtPercentile)
      })
    ,
    'DESCRIPTOR' : _SUMMARYVALUE_SNAPSHOT,
    '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
    # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.SummaryValue.Snapshot)
    })
  ,
  'DESCRIPTOR' : _SUMMARYVALUE,
  '__module__' : 'opencensus.proto.metrics.v1.metrics_pb2'
  # @@protoc_insertion_point(class_scope:opencensus.proto.metrics.v1.SummaryValue)
  })
_sym_db.RegisterMessage(SummaryValue)
_sym_db.RegisterMessage(SummaryValue.Snapshot)
_sym_db.RegisterMessage(SummaryValue.Snapshot.ValueAtPercentile)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036io.opencensus.proto.metrics.v1B\014MetricsProtoP\001ZDgithub.com/census-instrumentation/opencensus-proto/gen-go/metrics/v1\352\002\033OpenCensus.Proto.Metrics.V1'
  _DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY._options = None
  _DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY._serialized_options = b'8\001'
  _METRIC._serialized_start=185
  _METRIC._serialized_end=426
  _METRICDESCRIPTOR._serialized_start=429
  _METRICDESCRIPTOR._serialized_end=835
  _METRICDESCRIPTOR_TYPE._serialized_start=666
  _METRICDESCRIPTOR_TYPE._serialized_end=835
  _LABELKEY._serialized_start=837
  _LABELKEY._serialized_end=899
  _TIMESERIES._serialized_start=902
  _TIMESERIES._serialized_end=1119
  _LABELVALUE._serialized_start=1121
  _LABELVALUE._serialized_end=1184
  _POINT._serialized_start=1187
  _POINT._serialized_end=1512
  _DISTRIBUTIONVALUE._serialized_start=1515
  _DISTRIBUTIONVALUE._serialized_end=2358
  _DISTRIBUTIONVALUE_BUCKETOPTIONS._serialized_start=1816
  _DISTRIBUTIONVALUE_BUCKETOPTIONS._serialized_end=1976
  _DISTRIBUTIONVALUE_BUCKETOPTIONS_EXPLICIT._serialized_start=1934
  _DISTRIBUTIONVALUE_BUCKETOPTIONS_EXPLICIT._serialized_end=1968
  _DISTRIBUTIONVALUE_BUCKET._serialized_start=1978
  _DISTRIBUTIONVALUE_BUCKET._serialized_end=2093
  _DISTRIBUTIONVALUE_EXEMPLAR._serialized_start=2096
  _DISTRIBUTIONVALUE_EXEMPLAR._serialized_end=2358
  _DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY._serialized_start=2296
  _DISTRIBUTIONVALUE_EXEMPLAR_ATTACHMENTSENTRY._serialized_end=2358
  _SUMMARYVALUE._serialized_start=2361
  _SUMMARYVALUE._serialized_end=2856
  _SUMMARYVALUE_SNAPSHOT._serialized_start=2557
  _SUMMARYVALUE_SNAPSHOT._serialized_end=2856
  _SUMMARYVALUE_SNAPSHOT_VALUEATPERCENTILE._serialized_start=2783
  _SUMMARYVALUE_SNAPSHOT_VALUEATPERCENTILE._serialized_end=2856
# @@protoc_insertion_point(module_scope)

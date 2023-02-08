# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waves/events/grpc/blockchain_updates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves.events import events_pb2 as waves_dot_events_dot_events__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='waves/events/grpc/blockchain_updates.proto',
  package='waves.events.grpc',
  syntax='proto3',
  serialized_options=b'\n*com.wavesplatform.events.api.grpc.protobufZEgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/events/grpc\252\002\021Waves.Events.Grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*waves/events/grpc/blockchain_updates.proto\x12\x11waves.events.grpc\x1a\x19waves/events/events.proto\"\'\n\x15GetBlockUpdateRequest\x12\x0e\n\x06height\x18\x01 \x01(\x05\"I\n\x16GetBlockUpdateResponse\x12/\n\x06update\x18\x01 \x01(\x0b\x32\x1f.waves.events.BlockchainUpdated\"E\n\x1bGetBlockUpdatesRangeRequest\x12\x13\n\x0b\x66rom_height\x18\x01 \x01(\x05\x12\x11\n\tto_height\x18\x02 \x01(\x05\"P\n\x1cGetBlockUpdatesRangeResponse\x12\x30\n\x07updates\x18\x01 \x03(\x0b\x32\x1f.waves.events.BlockchainUpdated\":\n\x10SubscribeRequest\x12\x13\n\x0b\x66rom_height\x18\x01 \x01(\x05\x12\x11\n\tto_height\x18\x02 \x01(\x05\"A\n\x0eSubscribeEvent\x12/\n\x06update\x18\x01 \x01(\x0b\x32\x1f.waves.events.BlockchainUpdated2\xcd\x02\n\x14\x42lockchainUpdatesApi\x12\x65\n\x0eGetBlockUpdate\x12(.waves.events.grpc.GetBlockUpdateRequest\x1a).waves.events.grpc.GetBlockUpdateResponse\x12w\n\x14GetBlockUpdatesRange\x12..waves.events.grpc.GetBlockUpdatesRangeRequest\x1a/.waves.events.grpc.GetBlockUpdatesRangeResponse\x12U\n\tSubscribe\x12#.waves.events.grpc.SubscribeRequest\x1a!.waves.events.grpc.SubscribeEvent0\x01\x42\x87\x01\n*com.wavesplatform.events.api.grpc.protobufZEgithub.com/wavesplatform/gowaves/pkg/grpc/generated/waves/events/grpc\xaa\x02\x11Waves.Events.Grpcb\x06proto3'
  ,
  dependencies=[waves_dot_events_dot_events__pb2.DESCRIPTOR,])




_GETBLOCKUPDATEREQUEST = _descriptor.Descriptor(
  name='GetBlockUpdateRequest',
  full_name='waves.events.grpc.GetBlockUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='waves.events.grpc.GetBlockUpdateRequest.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=131,
)


_GETBLOCKUPDATERESPONSE = _descriptor.Descriptor(
  name='GetBlockUpdateResponse',
  full_name='waves.events.grpc.GetBlockUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='waves.events.grpc.GetBlockUpdateResponse.update', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=206,
)


_GETBLOCKUPDATESRANGEREQUEST = _descriptor.Descriptor(
  name='GetBlockUpdatesRangeRequest',
  full_name='waves.events.grpc.GetBlockUpdatesRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_height', full_name='waves.events.grpc.GetBlockUpdatesRangeRequest.from_height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_height', full_name='waves.events.grpc.GetBlockUpdatesRangeRequest.to_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=277,
)


_GETBLOCKUPDATESRANGERESPONSE = _descriptor.Descriptor(
  name='GetBlockUpdatesRangeResponse',
  full_name='waves.events.grpc.GetBlockUpdatesRangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='updates', full_name='waves.events.grpc.GetBlockUpdatesRangeResponse.updates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=279,
  serialized_end=359,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='waves.events.grpc.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_height', full_name='waves.events.grpc.SubscribeRequest.from_height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_height', full_name='waves.events.grpc.SubscribeRequest.to_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=419,
)


_SUBSCRIBEEVENT = _descriptor.Descriptor(
  name='SubscribeEvent',
  full_name='waves.events.grpc.SubscribeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='waves.events.grpc.SubscribeEvent.update', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=486,
)

_GETBLOCKUPDATERESPONSE.fields_by_name['update'].message_type = waves_dot_events_dot_events__pb2._BLOCKCHAINUPDATED
_GETBLOCKUPDATESRANGERESPONSE.fields_by_name['updates'].message_type = waves_dot_events_dot_events__pb2._BLOCKCHAINUPDATED
_SUBSCRIBEEVENT.fields_by_name['update'].message_type = waves_dot_events_dot_events__pb2._BLOCKCHAINUPDATED
DESCRIPTOR.message_types_by_name['GetBlockUpdateRequest'] = _GETBLOCKUPDATEREQUEST
DESCRIPTOR.message_types_by_name['GetBlockUpdateResponse'] = _GETBLOCKUPDATERESPONSE
DESCRIPTOR.message_types_by_name['GetBlockUpdatesRangeRequest'] = _GETBLOCKUPDATESRANGEREQUEST
DESCRIPTOR.message_types_by_name['GetBlockUpdatesRangeResponse'] = _GETBLOCKUPDATESRANGERESPONSE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeEvent'] = _SUBSCRIBEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBlockUpdateRequest = _reflection.GeneratedProtocolMessageType('GetBlockUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATEREQUEST,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.GetBlockUpdateRequest)
  })
_sym_db.RegisterMessage(GetBlockUpdateRequest)

GetBlockUpdateResponse = _reflection.GeneratedProtocolMessageType('GetBlockUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATERESPONSE,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.GetBlockUpdateResponse)
  })
_sym_db.RegisterMessage(GetBlockUpdateResponse)

GetBlockUpdatesRangeRequest = _reflection.GeneratedProtocolMessageType('GetBlockUpdatesRangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATESRANGEREQUEST,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.GetBlockUpdatesRangeRequest)
  })
_sym_db.RegisterMessage(GetBlockUpdatesRangeRequest)

GetBlockUpdatesRangeResponse = _reflection.GeneratedProtocolMessageType('GetBlockUpdatesRangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKUPDATESRANGERESPONSE,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.GetBlockUpdatesRangeResponse)
  })
_sym_db.RegisterMessage(GetBlockUpdatesRangeResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeEvent = _reflection.GeneratedProtocolMessageType('SubscribeEvent', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEEVENT,
  '__module__' : 'waves.events.grpc.blockchain_updates_pb2'
  # @@protoc_insertion_point(class_scope:waves.events.grpc.SubscribeEvent)
  })
_sym_db.RegisterMessage(SubscribeEvent)


DESCRIPTOR._options = None

_BLOCKCHAINUPDATESAPI = _descriptor.ServiceDescriptor(
  name='BlockchainUpdatesApi',
  full_name='waves.events.grpc.BlockchainUpdatesApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=489,
  serialized_end=822,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBlockUpdate',
    full_name='waves.events.grpc.BlockchainUpdatesApi.GetBlockUpdate',
    index=0,
    containing_service=None,
    input_type=_GETBLOCKUPDATEREQUEST,
    output_type=_GETBLOCKUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlockUpdatesRange',
    full_name='waves.events.grpc.BlockchainUpdatesApi.GetBlockUpdatesRange',
    index=1,
    containing_service=None,
    input_type=_GETBLOCKUPDATESRANGEREQUEST,
    output_type=_GETBLOCKUPDATESRANGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='waves.events.grpc.BlockchainUpdatesApi.Subscribe',
    index=2,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIBEEVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BLOCKCHAINUPDATESAPI)

DESCRIPTOR.services_by_name['BlockchainUpdatesApi'] = _BLOCKCHAINUPDATESAPI

# @@protoc_insertion_point(module_scope)

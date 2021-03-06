# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='simple_databroker',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndemo.proto\x12\x11simple_databroker\"_\n\rBrokerRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07sensor1\x18\x02 \x01(\x02\x12\x0f\n\x07sensor2\x18\x03 \x01(\x02\x12\x0f\n\x07sensor3\x18\x04 \x01(\x02\x12\x0f\n\x07sensor4\x18\x05 \x01(\x02\"0\n\x0e\x42rokerResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nprediction\x18\x02 \x01(\x08\x32\x64\n\rBrokerService\x12S\n\x0cSimpleMethod\x12 .simple_databroker.BrokerRequest\x1a!.simple_databroker.BrokerResponseb\x06proto3'
)




_BROKERREQUEST = _descriptor.Descriptor(
  name='BrokerRequest',
  full_name='simple_databroker.BrokerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='simple_databroker.BrokerRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor1', full_name='simple_databroker.BrokerRequest.sensor1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor2', full_name='simple_databroker.BrokerRequest.sensor2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor3', full_name='simple_databroker.BrokerRequest.sensor3', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor4', full_name='simple_databroker.BrokerRequest.sensor4', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=33,
  serialized_end=128,
)


_BROKERRESPONSE = _descriptor.Descriptor(
  name='BrokerResponse',
  full_name='simple_databroker.BrokerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='simple_databroker.BrokerResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='simple_databroker.BrokerResponse.prediction', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=130,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['BrokerRequest'] = _BROKERREQUEST
DESCRIPTOR.message_types_by_name['BrokerResponse'] = _BROKERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrokerRequest = _reflection.GeneratedProtocolMessageType('BrokerRequest', (_message.Message,), {
  'DESCRIPTOR' : _BROKERREQUEST,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:simple_databroker.BrokerRequest)
  })
_sym_db.RegisterMessage(BrokerRequest)

BrokerResponse = _reflection.GeneratedProtocolMessageType('BrokerResponse', (_message.Message,), {
  'DESCRIPTOR' : _BROKERRESPONSE,
  '__module__' : 'demo_pb2'
  # @@protoc_insertion_point(class_scope:simple_databroker.BrokerResponse)
  })
_sym_db.RegisterMessage(BrokerResponse)



_BROKERSERVICE = _descriptor.ServiceDescriptor(
  name='BrokerService',
  full_name='simple_databroker.BrokerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=180,
  serialized_end=280,
  methods=[
  _descriptor.MethodDescriptor(
    name='SimpleMethod',
    full_name='simple_databroker.BrokerService.SimpleMethod',
    index=0,
    containing_service=None,
    input_type=_BROKERREQUEST,
    output_type=_BROKERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROKERSERVICE)

DESCRIPTOR.services_by_name['BrokerService'] = _BROKERSERVICE

# @@protoc_insertion_point(module_scope)

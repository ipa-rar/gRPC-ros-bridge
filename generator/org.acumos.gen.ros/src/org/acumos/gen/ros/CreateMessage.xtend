/*****************************************************************************
 * Copyright (c) 2021 CEA LIST.
 * 
 * 
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * https://www.eclipse.org/legal/epl-2.0/
 * 
 *****************************************************************************/
 
 package org.acumos.gen.ros

import com.google.protobuf.DescriptorProtos.DescriptorProto
import com.google.protobuf.Descriptors.FieldDescriptor
import java.util.List
import com.google.protobuf.DescriptorProtos.FieldDescriptorProto
import java.util.ArrayList
import com.google.protobuf.DescriptorProtos.ServiceDescriptorProto

class CreateMessage {
	/**
	 * Create contents for a proto message type
	 */
	static def createMessage(DescriptorProto msgType) '''
		# fields of message type «msgType.name»
		«FOR fieldKey : msgType.allFields.keySet»
			«FOR field : getFields(msgType, fieldKey)»
««« TODO take "repeated" and "options" into account
				«TrafoUtils.rosType(field)» «field.name»
			«ENDFOR»
		«ENDFOR»
	'''

	/**
	 * Create contents for a proto service (RCP)
	 */
	static def createService(ServiceDescriptorProto serviceType) '''
		# fields of service type «serviceType.name»
		«FOR method : serviceType.methodList»
««« TODO mapping to query is likely not right
			«method.inputType.substring(1)» request
			---
			«method.outputType.substring(1)» reply
		«ENDFOR»
	'''
		
	/**
	 * Return a set of field descriptor protos
	 */
	static def getFields(DescriptorProto msgType, FieldDescriptor fieldKey) {
		val fieldList = new ArrayList<FieldDescriptorProto>()
		var fields = msgType.allFields.get(fieldKey)
		if (fields instanceof List) {
			for (field : fields) {
				if (field instanceof FieldDescriptorProto) {
					fieldList.add(field)
				}
			}
		}
		return fieldList;
	}
}
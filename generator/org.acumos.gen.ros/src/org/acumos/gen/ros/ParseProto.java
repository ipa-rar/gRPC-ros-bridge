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

package org.acumos.gen.ros;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

import com.google.protobuf.DescriptorProtos.DescriptorProto;
import com.google.protobuf.DescriptorProtos.FileDescriptorProto;
import com.google.protobuf.DescriptorProtos.FileDescriptorSet;
import com.google.protobuf.DescriptorProtos.ServiceDescriptorProto;
import com.google.protobuf.Descriptors;
import com.google.protobuf.Descriptors.DescriptorValidationException;
import com.google.protobuf.InvalidProtocolBufferException;

/**
 * Parse a proto descriptor set
 */
public class ParseProto {
	private static final String DS_FILE = "/local/home/ansgar/git/ai4eu/test/demo.ds"; //$NON-NLS-1$

	/**
	 * Return a proto file descriptor from a compiled file (descriptor set)
	 * 
	 * @param dsFileName
	 *            a descriptor-set file (create e.g. with "protoc --descriptor_set_out")
	 * @return the obtained file descriptor
	 *
	 * @throws InvalidProtocolBufferException
	 * @throws Descriptors.DescriptorValidationException
	 * @throws FileNotFoundException 
	 */
	public static FileDescriptorProto getDescriptor(String dsFileName) throws InvalidProtocolBufferException, Descriptors.DescriptorValidationException, FileNotFoundException {
		InputStream is = new FileInputStream(dsFileName);
		FileDescriptorProto proto = null;
		try {
			byte data[] = is.readAllBytes();
			FileDescriptorSet protoSet = FileDescriptorSet.parseFrom(data);
			// DescriptorProtos.FileDescriptorProto descriptorProto = DescriptorProtos.FileDescriptorProto.parseFrom(x);
			proto = protoSet.getFileList().iterator().next();
			// proto = Descriptors.FileDescriptor.buildFrom(descriptorProto, new Descriptors.FileDescriptor[0]);
			is.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return proto;
	}

	public static void main(String args[]) {
		try {
			FileDescriptorProto proto = getDescriptor(args.length > 0 ? args[0] : DS_FILE);
			for (DescriptorProto msgType : proto.getMessageTypeList()) {
				System.err.println();
				System.err.println(CreateMessage.createMessage(msgType));
			}
			for (ServiceDescriptorProto svcType : proto.getServiceList()) {
				// System.err.println(CreateMessage.createService(svcType));
			}
			System.err.println();
			System.err.println("CMakeLists.txt:"); //$NON-NLS-1$
			System.err.println(CreateBuildFiles.createCMakeLists(proto));

			System.err.println();
			System.err.println("package.xml:"); //$NON-NLS-1$
			System.err.println(CreateBuildFiles.createPackageXML(proto));
	
		} catch (InvalidProtocolBufferException | DescriptorValidationException | FileNotFoundException e) {
			e.printStackTrace();
		}
	}
}

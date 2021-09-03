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

import com.google.protobuf.DescriptorProtos.FieldDescriptorProto;

/**
 * Utility functions for creating ROS from a .proto file
 */
public class TrafoUtils {

	private static final String PROTO_EXT = ".proto"; //$NON-NLS-1$

	@SuppressWarnings("nls")
	static final String[][] mapping = new String[][] {
			{ "TYPE_BOOL", "bool" },
			{ "TYPE_OCTETS", "byte[]" },
			{ "TYPE_INT32", "int32" },
			{ "TYPE_UINT32", "uint32" },
			{ "TYPE_FLOAT", "float32" },
			{ "TYPE_DOUBLE", "float64" },
	};

	/**
	 * Map proto type names to ROS type names (might be incomplete)
	 */
	public static String rosType(FieldDescriptorProto field) {
		String type = field.getType().name();

		for (String[] mapEntry : mapping) {
			if (mapEntry[0].equals(type)) {
				return mapEntry[1];
			}
		}
		return type;
	}

	/**
	 * Remove .proto extension from a proto file name
	 * 
	 * @param name
	 * @return the stripped name if the extension was found, the original name otherwise.
	 */
	public static String stripExt(String name) {
		if (name.endsWith(PROTO_EXT)) {
			return name.substring(0, name.length() - PROTO_EXT.length());
		}
		return name;
	}
}

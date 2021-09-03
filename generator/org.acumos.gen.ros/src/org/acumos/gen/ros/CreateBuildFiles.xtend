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

import com.google.protobuf.DescriptorProtos.FileDescriptorProto

import static extension org.acumos.gen.ros.TrafoUtils.*

class CreateBuildFiles {
	/**
	 * Create contents for a proto message type
	 */
	static def createCMakeLists(FileDescriptorProto proto) '''
		cmake_minimum_required(VERSION 4.5)
		project(«proto.name.stripExt»_msgs)
		
		# Default to C99
		if(NOT CMAKE_C_STANDARD)
			set(CMAKE_C_STANDARD 99)
		endif()
		
		# Default to C++14
		if(NOT CMAKE_CXX_STANDARD)
			set(CMAKE_CXX_STANDARD 14)
		endif()
		
		if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
			add_compile_options(-Wall -Wextra -Wpedantic)
		endif()
		
		# find dependencies
		find_package(ament_cmake REQUIRED)
		# uncomment the following section in order to fill in
		# further dependencies manually.
		# find_package(<dependency> REQUIRED)
		##############################################
		find_package(rosidl_default_generators REQUIRED)
		rosidl_generate_interfaces(${PROJECT_NAME}
			«FOR msgType : proto.messageTypeList»
				"msg/«msgType.name».msg"
			«ENDFOR»
		)
		##############################################
		
		if(BUILD_TESTING)
			find_package(ament_lint_auto REQUIRED)
			# the following line skips the linter which checks for copyrights
			# uncomment the line when a copyright and license is not present in all source files
			#set(ament_cmake_copyright_FOUND TRUE)
			# the following line skips cpplint (only works in a git repo)
			# uncomment the line when this package is not in a git repo
			#set(ament_cmake_cpplint_FOUND TRUE)
			ament_lint_auto_find_test_dependencies()
		endif()
		
		ament_package()
	'''

	static def createPackageXML(FileDescriptorProto proto) '''
		<?xml version="1.0"?>
		<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
		<package format="3">
			<name>«proto.name.stripExt»_msgs</name>
			<version>0.0.0</version>
			<description>generated from proto "«proto.name»" in package "«proto.package»"</description>
			<maintainer email="ragesh.ramachandran@ipa.fraunhofer.de">TODO ragesh_ramachandran</maintainer>
			<license>TODO: License declaration</license>

			<buildtool_depend>ament_cmake</buildtool_depend>
			<depend>rclpy</depend>

			<build_depend>rosidl_default_generators</build_depend>
			<exec_depend>rosidl_default_runtime</exec_depend>
			<member_of_group>rosidl_interface_packages</member_of_group>

			<test_depend>ament_lint_auto</test_depend>
			<test_depend>ament_lint_common</test_depend>

			<export>
				<build_type>ament_cmake</build_type>
			</export>
		</package>
	'''

}

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# 
###############################################################################
# Module:    exceptions
# Purpose:   Collection of custom exceptions for the applier package
#
# Notes:
#
###############################################################################


class ApplyError(Exception):
    """Exceptions raised when an unsupported DbType is used.

    Attributes:
        dbtype -- the DbType that was used
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

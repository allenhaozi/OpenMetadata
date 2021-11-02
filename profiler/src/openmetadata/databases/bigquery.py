#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from typing import Optional, Tuple

from openmetadata.common.database_common import (
    DatabaseCommon,
    SQLConnectionConfig,
    SQLExpressions,
)


class BigqueryConfig(SQLConnectionConfig):
    scheme = "bigquery"
    project_id: Optional[str] = None
    duration: int = 1
    service_type = "BigQuery"

    def get_connection_url(self):
        if self.project_id:
            return f"{self.scheme}://{self.project_id}"
        return f"{self.scheme}://"


class BigquerySQLExpressions(SQLExpressions):
    stddev_expr = "STDDEV_POP({})"
    regex_like_pattern_expr = "REGEXP_CONTAINS({expr}, r'{}')"


class Bigquery(DatabaseCommon):
    config: BigqueryConfig = None
    sql_exprs: BigquerySQLExpressions = BigquerySQLExpressions()

    def __init__(self, config):
        super().__init__(config)
        self.config = config

    @classmethod
    def create(cls, config_dict):
        config = BigqueryConfig.parse_obj(config_dict)
        return cls(config)

    def qualify_table_name(self, table_name: str) -> str:
        return f"`{self.config.database}.{table_name}`"
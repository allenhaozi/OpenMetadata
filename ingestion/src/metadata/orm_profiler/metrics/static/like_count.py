#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Like Count Metric definition
"""
from sqlalchemy import case, func

from metadata.orm_profiler.metrics.core import StaticMetric, _label


class LikeCount(StaticMetric):
    """
    LIKE_COUNT Metric

    Given a column, and an expression, return the number of
    rows that match it
    """

    @classmethod
    def name(cls):
        return "likeCount"

    @property
    def metric_type(self):
        return int

    @_label
    def fn(self):
        if not hasattr(self, "expression"):
            raise AttributeError(
                "Like Count requires an expression to be set: add_props(expression=...)(Metrics.LIKE_COUNT)"
            )
        return func.sum(case([(self.col.like(self.expression), 1)], else_=0))

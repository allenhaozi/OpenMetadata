# generated by datamodel-codegen:
#   filename:  schema/api/policies/createPolicy.json
#   timestamp: 2021-12-02T02:38:07+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...entity.policies import policy
from ...type import entityReference


class CreatePolicyEntityRequest(BaseModel):
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this Policy.'
    )
    displayName: Optional[str] = Field(None, description='Title for this Policy.')
    description: str = Field(
        ...,
        description='A short description of the Policy, comprehensible to regular users.',
    )
    owner: entityReference.EntityReference = Field(
        ..., description='Owner of this Policy.'
    )
    policyUrl: Optional[AnyUrl] = Field(
        None, description='Link to a well documented definition of this Policy.'
    )
    policyType: policy.PolicyType
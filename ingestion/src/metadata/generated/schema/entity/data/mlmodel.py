# generated by datamodel-codegen:
#   filename:  schema/entity/data/mlmodel.json
#   timestamp: 2021-12-02T02:38:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel, usageDetails


class FeatureType(Enum):
    numerical = 'numerical'
    categorical = 'categorical'


class FeatureSourceDataType(Enum):
    integer = 'integer'
    number = 'number'
    string = 'string'
    array = 'array'
    date = 'date'
    timestamp = 'timestamp'
    object = 'object'
    boolean = 'boolean'


class FeatureName(BaseModel):
    __root__: constr(regex=r'^[^.]*$', min_length=1, max_length=64) = Field(
        ..., description='Local name (not fully qualified name) of the ML Feature.'
    )


class FeatureSourceName(BaseModel):
    __root__: constr(regex=r'^[^.]*$', min_length=1, max_length=64) = Field(
        ..., description='Local name (not fully qualified name) of a ML Feature source.'
    )


class FullyQualifiedFeatureSourceName(BaseModel):
    __root__: constr(min_length=1, max_length=256) = Field(
        ...,
        description='Fully qualified name of the ML Feature Source that includes `serviceName.[databaseName].tableName/fileName/apiName.columnName[.nestedColumnName]`.',
    )


class FullyQualifiedFeatureName(BaseModel):
    __root__: constr(min_length=1, max_length=256) = Field(
        ...,
        description='Fully qualified name of the ML Feature that includes `modelName.featureName`.',
    )


class MlHyperParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Hyper parameter name.')
    value: Optional[str] = Field(None, description='Hyper parameter value.')
    description: Optional[str] = Field(
        None, description='Description of the Hyper Parameter.'
    )


class FeatureSource(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[FeatureSourceName] = None
    dataType: Optional[FeatureSourceDataType] = Field(
        None, description='Data type of the source (int, date etc.).'
    )
    description: Optional[str] = Field(
        None, description='Description of the feature source.'
    )
    fullyQualifiedName: Optional[FullyQualifiedFeatureSourceName] = None
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags associated with the feature source.'
    )


class MlFeature(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[FeatureName] = None
    dataType: Optional[FeatureType] = Field(
        None, description='Data type of the column (numerical vs. categorical).'
    )
    description: Optional[str] = Field(
        None, description='Description of the ML Feature.'
    )
    fullyQualifiedName: Optional[FullyQualifiedFeatureName] = None
    featureSources: Optional[List[FeatureSource]] = Field(
        None, description='Columns used to create the ML Feature.'
    )
    featureAlgorithm: Optional[str] = Field(
        None,
        description='Description of the algorithm used to compute the feature, e.g., PCA, bucketing...',
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags associated with the feature.'
    )


class MlModel(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier of an ML Model instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this ML Model.'
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None, description='A unique name that identifies an ML Model.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this ML Model.'
    )
    description: Optional[str] = Field(
        None, description='Description of the ML Model, what it is, and how to use it.'
    )
    algorithm: str = Field(..., description='Algorithm used to train the ML Model.')
    mlFeatures: Optional[List[MlFeature]] = Field(
        None, description='Features used to train the ML Model.'
    )
    mlHyperParameters: Optional[List[MlHyperParameter]] = Field(
        None, description='Hyper Parameters used to train the ML Model.'
    )
    dashboard: Optional[entityReference.EntityReference] = Field(
        None, description='Performance Dashboard URL to track metric evolution.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this ML Model.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this ML Model.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this ML Model.'
    )
    usageSummary: Optional[usageDetails.TypeUsedToReturnUsageDetailsOfAnEntity] = Field(
        None, description='Latest usage information for this ML Model.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
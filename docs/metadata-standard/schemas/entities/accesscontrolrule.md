# Access Control Rule

Describes an Access Control Rule for OpenMetadata Metadata Operations. All non-null user (subject) and entity (object) attributes are evaluated with logical AND.

**$id:** [**https://open-metadata.org/schema/entity/data/policies/accessControl/rule.json**](https://open-metadata.org/schema/entity/policies/accessControl/rule.json)

Type: `object`

This schema does not accept additional properties.

## Properties

* **name** `required`
  * Name for this Rule.
  * Type: `string`
* **entityTypeAttr**
  * Entity type that the rule should match on.
  * Type: `string`
* **entityTagAttr**
  * Entity tag that the rule should match on.
  * $ref: [../../type/tagLabel.json#/definitions/tagFQN](../types/taglabel.md#tagfqn)
* **userRoleAttr**
  * Role of the user that the rule should match on.
  * $ref: [../teams/team.json#/definitions/teamName](team.md#teamname)
* **operation**
  * Operation on the entity.
  * $ref: [#/definitions/operation](accesscontrolrule.md#operation)
* **allow**
  * Allow or Deny operation on the entity.
  * Type: `boolean`
  * Default: _false_
* **priority**
  * Priority of this rule among all rules across all policies.
  * Type: `integer`
  * Default: `250000`
* **enabled**
  * Is the rule enabled.
  * Type: `boolean`
  * Default: _true_

## Type definitions in this schema

### operation

* This schema defines all possible operations on metadata of data entities.
* Type: `string`
* The value is restricted to the following:
  1. _"SuggestDescription"_
  2. _"SuggestTags"_
  3. _"UpdateDescription"_
  4. _"UpdateOwner"_
  5. _"UpdateTags"_
  6. _"UpdateLineage"_

_This document was updated on: Tuesday, January 25, 2022_
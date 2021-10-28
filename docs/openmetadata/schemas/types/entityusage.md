# Entity Usage

This schema defines the type used for capturing usage details of an entity.

**$id: **[**https://open-metadata.org/schema/type/entityUsage.json**](https://open-metadata.org/schema/type/entityUsage.json)

Type: `object`

## Properties

* **entity** `required`
  * Entity for which usage is returned.
  * $ref: [entityReference.json](entityreference.md)
* **usage** `required`
  * List usage details per day.
  * Type: `array`
    * **Items**
    * $ref: [usageDetails.json](usagedetails.md)

_This document was updated on: Monday, October 18, 2021_
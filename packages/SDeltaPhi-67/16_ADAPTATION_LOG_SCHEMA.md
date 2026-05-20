# Adaptation Log Schema

Every local adaptation should record what changed.

## Required fields

```text
adapter_id
adapter_version
base_sdelta_version
modified_routing_rules
modified_thresholds
required_modules
disabled_modules
reason_for_adaptation
compatibility_test_result
known_risks
review_date
reviewer_or_system
```

## Rule

If an adapter cannot explain what changed, it should not be treated as compatible.

## Function

Adaptation logs prevent silent mutation.

They also make local routing decisions auditable across versions.

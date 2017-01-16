from decimal import Decimal

from corehq.apps.accounting.models import (
    FeatureType,
    SoftwarePlanEdition,
)

BOOTSTRAP_CONFIG = {
    (SoftwarePlanEdition.COMMUNITY, False): {
        'role': 'community_plan_v1',
        'product_rate': dict(),
        'feature_rates': {
            FeatureType.USER: dict(monthly_limit=10, per_excess_fee=Decimal('2.00')),
            FeatureType.SMS: dict(monthly_limit=0),
        }
    },
    (SoftwarePlanEdition.STANDARD, False): {
        'role': 'standard_plan_v0',
        'product_rate': dict(),
        'feature_rates': {
            FeatureType.USER: dict(monthly_limit=50, per_excess_fee=Decimal('2.00')),
            FeatureType.SMS: dict(monthly_limit=100),
        }
    },
    (SoftwarePlanEdition.PRO, False): {
        'role': 'pro_plan_v0',
        'product_rate': dict(),
        'feature_rates': {
            FeatureType.USER: dict(monthly_limit=250, per_excess_fee=Decimal('2.00')),
            FeatureType.SMS: dict(monthly_limit=500),
        }
    },
    (SoftwarePlanEdition.ADVANCED, False): {
        'role': 'advanced_plan_v0',
        'product_rate': dict(),
        'feature_rates': {
            FeatureType.USER: dict(monthly_limit=500, per_excess_fee=Decimal('2.00')),
            FeatureType.SMS: dict(monthly_limit=1000),
        }
    },
    (SoftwarePlanEdition.ADVANCED, True): {
        'role': 'advanced_plan_v0',
        'product_rate': dict(),
        'feature_rates': {
            FeatureType.USER: dict(monthly_limit=10, per_excess_fee=Decimal('2.00')),
            FeatureType.SMS: dict(monthly_limit=0),
        }
    }
}
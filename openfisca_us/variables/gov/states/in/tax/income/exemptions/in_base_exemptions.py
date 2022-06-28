from openfisca_us.model_api import *


class in_base_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "IN base exemptions"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        num_filers = tax_unit("num", period)
        base_exemption = p.base.amount
        dependents = tax_unit("tax_unit_dependents", period)
        return (dependents + num_filers) * base_exemption

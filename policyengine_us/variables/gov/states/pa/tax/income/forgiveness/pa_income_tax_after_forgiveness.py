from policyengine_us.model_api import *


class pa_income_tax_after_forgiveness(Variable):
    value_type = float
    entity = TaxUnit
    label = "PA income tax after forgiveness"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2021/2021_pa-40in.pdf#page=21"
    defined_for = StateCode.PA

    def formula(tax_unit, period, parameters):
        tax_before_forgiveness = tax_unit(
            "pa_income_tax_before_forgiveness", period
        )
        forgiveness = tax_unit("pa_tax_forgiveness_amount", period)
        return tax_before_forgiveness - forgiveness

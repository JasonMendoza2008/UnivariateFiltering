import pandas as pd
import statsmodels.discrete.discrete_model  # for type-hinting purposes
import statsmodels.formula.api as smf

from create_dataframe import DataStratification, create_dataframe

if __name__ == "__main__":

    example_number: int
    for example_number in [0, 1]:
        print(f"\n\n EXAMPLE_NUMBER {example_number}\n\n")
        df_all: pd.DataFrame = create_dataframe(
            which_data=DataStratification.ALL,
            manim=False,
            example_number=example_number,
        )


        # Univariate (Sex)
        model_u_s: statsmodels.discrete.discrete_model.Logit = smf.logit(
            formula=f"CAD ~ C(Male, Treatment(reference=1))",
            data=df_all
        )
        res_u_s: statsmodels.discrete.discrete_model.BinaryResultsWrapper = model_u_s.fit()

        print("Univariate (Sex)", res_u_s.summary())


        # Univariate (Activity)
        model_u_a: statsmodels.discrete.discrete_model.Logit = smf.logit(
            formula=f"CAD ~ C(Activity, Treatment(reference=1))",
            data=df_all
        )
        res_u_a: statsmodels.discrete.discrete_model.BinaryResultsWrapper = model_u_a.fit()

        print("Univariate (Activity)", res_u_a.summary())


        # Multivariate (Sex & Activity)
        model_m: statsmodels.discrete.discrete_model.Logit = smf.logit(
            formula=f"CAD ~ C(Activity, Treatment(reference=1)) + C(Male, Treatment(reference=1))",
            data=df_all
        )
        res_m: statsmodels.discrete.discrete_model.BinaryResultsWrapper = model_m.fit()

        print("Multivariate", res_m.summary())
        print(res_m.pvalues)

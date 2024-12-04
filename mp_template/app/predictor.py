
import math

# the means and stds and betas are exported from the training notebook

means = [1.99325361e+08, 2.18490011e+08, 1.86095959e+01, 2.70340170e+01, 2.78634426e+07, 6.48462882e-01, 9.10653930e-01, 1.60578868e+17]

stds = [2.23797754e+08, 2.47824979e+08, 1.07211860e+00, 1.37705381e+00, 4.43763103e+07, 9.74616918e-02, 5.35356772e-01, 2.70388905e+17]

models = {
    "Total Emissions": {
        "beta_0": 653687.64558036,
        "betas": [599782.62815931,95057.33815046,183236.79974751,221850.18082905,-149983.24431753,27023.45681085,-109388.2144206,-413952.62006661],
    },
    "Industrial Processes Product Use": {
        "beta_0": 224006.24034231,
        "betas": [ 410805.43597673, 137196.6902314, -11188.42922434, -1995.57737677, 2538.44316684, 14183.20422837, 17663.35930106, -211917.20406152],
    },
    "Food Household": {
        "beta_0": 55328.89668463,
        "betas": [ 95591.4654611, 31853.49325778, -2432.33274453, -537.20259854, -1512.75111925, 4866.19646377, 3344.83591832, -46592.28187464],
    },
    "Agrifood Systems Waste Disposal": {
        "beta_0": 75322.1526699,
        "betas": [20237.87309589, 12859.34627837, 18484.01502922, 13356.60532086, 261.96071875, -236.79412889, -6282.53176893, 6408.18498093],
    },
    "Net forest conversion": {
        "beta_0": 181461.97120685,
        "betas": [-61412.69977048, -173974.6048344, 165100.78499661, 207101.06022837, -39879.54305977, 3112.18760612, -105324.36475251, -154670.17147027],
    },
    "Rice cultivation": {
        "beta_0": 51929.59936863,
        "betas": [17371.74732224, 19018.41281277, 13398.3889624, -8589.98850935, -4808.17000805, -440.0788472, -1515.87182144, 12005.87451384],
    },
}

def predict_all_emission_sources(
    total_population: float,
    gdp_per_capita: float,
    percentage_male: float,
    percentage_urban: float,
    human_development_index: float,
    temperature_increase: float,
) -> list[dict]:
    """ Predicts the agricultural emissions of a country. """

    urban_population = total_population * (percentage_urban / 100)
    rural_population = total_population - urban_population
    male_population = total_population * (percentage_male / 100)
    female_population = total_population - male_population

    ordered_values = [
        total_population,
        female_population,
        math.log(male_population),
        math.log(gdp_per_capita * total_population),
        gdp_per_capita**2,
        human_development_index,
        temperature_increase,
        rural_population**2
    ]

    predictions = []

    for model_name, model in models.items():
        prediction = model["beta_0"]
        for beta, mean, std, value in zip(model["betas"], means, stds, ordered_values):
            prediction += beta * ((value - mean) / std)
        predictions.append({
            "source": model_name,
            "value": prediction,
        })

    return predictions


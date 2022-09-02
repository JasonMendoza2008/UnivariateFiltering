import pandas as pd
from enum import Enum, auto

class DataStratification(Enum):
    INACTIVE = 0
    ACTIVE = 1
    ALL = 2


def create_dataframe(
        which_data: DataStratification = DataStratification.ALL,
        manim: bool = False,
        example_number: int = 0
) -> pd.DataFrame:
    """
    :param manim: whether or not the dataframe desired is the one to be displayed or the one to be used by statsmodels
    :param which_data: only matters if manim=True
    :param example_number: basic example or slighty changed example to show a higher cut-off does not change nothing

    :return: the desired pandas Dataframe
    """

    # Initialisation
    if example_number == 0:
        i_c_f: int = 80
        i_c_m: int = 84
        i_n_f: int = 800
        i_n_m: int = 1200
        a_c_f: int = 33
        a_c_m: int = 10
        a_n_f: int = 1200
        a_n_m: int = 800
        ia_c_f: int = 113
        ia_c_m: int = 94
        ia_n_f: int = 2000
        ia_n_m: int = 2000
    else:
        i_c_f: int = 70
        i_c_m: int = 84
        i_n_f: int = 750
        i_n_m: int = 1250
        a_c_f: int = 38
        a_c_m: int = 10
        a_n_f: int = 1250
        a_n_m: int = 750
        ia_c_f: int = 108
        ia_c_m: int = 94
        ia_n_f: int = 2000
        ia_n_m: int = 2000

    # Sanity checks
    assert (ia_c_f == i_c_f + a_c_f)
    assert (ia_c_m == i_c_m + a_c_m)
    assert (ia_n_f == i_n_f + a_n_f)
    assert (ia_n_m == i_n_m + a_n_m)

    # Dataframe creation
    if manim:
        if which_data == DataStratification.INACTIVE:
            df = pd.DataFrame(
                data={
                    'Coronary Artery disease': [i_c_f, i_c_m],
                    'Non-Coronary Artery disease': [i_n_f, i_n_m]
                },
                index=[
                    "Female",
                    "Male",
                ]
            )
        elif which_data == DataStratification.ACTIVE:
            df = pd.DataFrame(
                data={
                    'Coronary Artery disease': [a_c_f, a_c_m],
                    'Non-Coronary Artery disease': [a_n_f, a_n_m]
                },
                index=[
                    "Female",
                    "Male",
                ]
            )
        else:
            assert (which_data == DataStratification.ALL)

            df = pd.DataFrame(
                data={
                    'Coronary Artery disease': [ia_c_f, ia_c_m],
                    'Non-Coronary Artery disease': [ia_n_f, ia_n_m]
                },
                index=[
                    "Female",
                    "Male",
                ]
            )


    else:
        # encoding for column Male: female = 0, male = 1
        df = pd.DataFrame(
            data={
                'CAD': i_c_f*[1]+i_c_m*[1]+i_n_f*[0]+i_n_m*[0]+a_c_f*[1]+a_c_m*[1]+a_n_f*[0]+a_n_m*[0],
                'Activity': i_c_f*[0]+i_c_m*[0]+i_n_f*[0]+i_n_m*[0]+a_c_f*[1]+a_c_m*[1]+a_n_f*[1]+a_n_m*[1],
                'Male': i_c_f*[0]+i_c_m*[1]+i_n_f*[0]+i_n_m*[1]+a_c_f*[0]+a_c_m*[1]+a_n_f*[0]+a_n_m*[1],
            }
        )

    return df

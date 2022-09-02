from manim import *

from create_dataframe import DataStratification, create_dataframe


class HypotheticalExample(Scene):
    def construct(self):
        example_number: int
        p_values_list: list[str]
        beta_list: list[str]
        or_list: list[str]
        for example_number, p_values_list, beta_list, or_list in zip(
                [0, 1],
                [
                    ["0.198", "3.045*10^{-3}", "7.489*10^{-16}"],
                    ["0.337>0.2", "4.294*10^{-3}", "1.627*10^{-13}"],
                ],
                [
                    ["0.1841", "0.4339", "1.4254"],
                    ["0.1388", "0.4258", "1.2722"],
                ],
                [
                    ["1.20", "1.54", "4.16"],
                    ["1.15", "1.53", "3.56"],
                ]
        ):
            # Initialisation
            df_all: pd.DataFrame = create_dataframe(
                which_data=DataStratification.ALL,
                manim=True,
                example_number=example_number,
            )
            df_active: pd.DataFrame = create_dataframe(
                which_data=DataStratification.ACTIVE,
                manim=True,
                example_number=example_number,
            )
            df_inactive: pd.DataFrame = create_dataframe(
                which_data=DataStratification.INACTIVE,
                manim=True,
                example_number=example_number,
            )

            # Animations
            self.next_section(name=f"RawTable_{example_number}_0")

            t_all: Table = Table(
                df_all.astype(str).to_numpy(),
                row_labels=[Text("Female"), Text("Male")],
                col_labels=[Text("CAD"), Text("Non-CAD")],
            ).move_to(UP*1.5)

            p_value_univariate: MathTex = MathTex(
                f"Female: \\beta_0 \\approx {beta_list[0]} \: (OR_0 \\approx {or_list[0]}) \:\: "
                f"p \\approx {p_values_list[0]}"
            ).move_to(DOWN*1.5)

            self.play(
                Write(t_all)
            )

            self.next_section(name=f"RawTable_{example_number}_1")

            temp_t_all: Table = t_all.copy()
            temp_t_all.add_highlighted_cell((2, 2), color=GREEN)  # noqa (manim type-hinting is wrong)
            self.play(FadeTransform(t_all, temp_t_all))

            self.next_section(name=f"RawTable_{example_number}_2")

            temp_t_all_2: Table = t_all.copy()
            temp_t_all_2.add_highlighted_cell((2, 3), color=GREEN)  # noqa (manim type-hinting is wrong)
            self.play(FadeTransform(temp_t_all, temp_t_all_2))

            self.next_section(name=f"RawTable_{example_number}_3")

            temp_t_all_3: Table = t_all.copy()
            temp_t_all_3.add_highlighted_cell((3, 2), color=GREEN)  # noqa (manim type-hinting is wrong)
            self.play(FadeTransform(temp_t_all_2, temp_t_all_3))

            self.next_section(name=f"RawTable_{example_number}_4")

            temp_t_all_4: Table = t_all.copy()
            temp_t_all_4.add_highlighted_cell((3, 3), color=GREEN)  # noqa (manim type-hinting is wrong)
            self.play(FadeTransform(temp_t_all_3, temp_t_all_4))

            self.next_section(name=f"RawTable_{example_number}_5")

            self.play(FadeTransform(temp_t_all_4, t_all))  # on enlève l'highlight
            self.play(
                Write(p_value_univariate)
            )

            self.next_section(name=f"RawTable_{example_number}_6")

            p_value_multivariate: MathTex = MathTex(
                f"""
                Female&: \\beta_0 \\approx {beta_list[1]} \: (OR_0 \\approx {or_list[1]}) \:\: 
                p \\approx {p_values_list[1]}
                \\\\
                Inactive&: \\beta_1 \\approx {beta_list[2]} \: (OR_1 \\approx {or_list[2]}) \:\: 
                p \\approx {p_values_list[2]}
                """
            ).move_to(DOWN*1.5)

            self.play(
                Transform(p_value_univariate, p_value_multivariate)
            )

            self.next_section(name=f"RawTable_{example_number}_7")

            self.play(
                Unwrite(p_value_univariate)
            )

            active_label: Text = Text(
                "Active"
            ).move_to((2*UP + 2*RIGHT)*1.75).scale(0.8)
            t_active: Table = Table(
                df_active.astype(str).to_numpy(),
                row_labels=[Text("Female"), Text("Male")],
                col_labels=[Text("CAD"), Text("Non-CAD")],
            ).move_to((1.015*UP + 2*RIGHT)*1.75).scale(0.6)

            inactive_label: Text = Text(
                "Inactive"
            ).move_to((2*UP + 2*LEFT)*1.75).scale(0.8)
            t_inactive: Table = Table(
                df_inactive.astype(str).to_numpy(),
                row_labels=[Text("Female"), Text("Male")],
                col_labels=[Text("CAD"), Text("Non-CAD")],
            ).move_to((UP + 2*LEFT)*1.75).scale(0.6)

            self.play(
                Transform(t_all, t_inactive),  # t_active will be named t_all from now on in the code
                Write(inactive_label),
                Write(t_active),
                Write(active_label),
            )

            self.next_section(name=f"RawTable_{example_number}_8")

            self.play(
                *[FadeOut(mob) for mob in self.mobjects], run_time=0.5
            )

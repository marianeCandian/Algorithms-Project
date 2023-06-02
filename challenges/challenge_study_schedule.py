def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    estudantes_presentes = 0

    for intervalo in permanence_period:
        entrada, saida = intervalo

        if type(entrada) != int or type(saida) != int:
            return None

        for tempo in range(entrada, saida + 1):
            if tempo == target_time:
                estudantes_presentes += 1

    return estudantes_presentes


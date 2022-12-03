# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:01:26 2022

@author: fernandomacchiavellocauvi
"""

from colorama import Back
from colorama import Style
from colorama import Fore
import pandas as pd
import operator


import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

# terminal colors

true_bracket = r"C:\Users\user\Documents\Mundial\true_bracket.csv"

cuartos_set = set()
semis_set = set()
final_set = set()
ganador_set = set()
tercero_set = set()
grupos = []

# person_to_file = {
#     "Maximum Points Possible": true_bracket,
#     "Allen": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/allen.csv",
#     "Agustin": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/agustin.csv",
#     "Alexander": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/alexander.csv",
#     "Cata": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/cata.csv",
#     "Fernando": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/fernando.csv",
#     "Hasan": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/hasan.csv",
#     "Ivan": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/ivan.csv",
#     "Kavi K": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/kavi_k.csv",
#     "Luiza": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/luiza.csv",
#     "Jaco": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/jaco.csv",
#     "Pablo B": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/pablo_b.csv",
#     "Pablo T": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/pablo_t.csv",
#     "Sofia G": "/Users/fernandomacchiavellocauvi/Downloads/Mundial/People/sofia_g.csv",
# }

person_to_file = {
    "Maximum Points Possible": true_bracket,
    "Allen": r"C:\Users\user\Documents\Mundial\People/allen.csv",
    "Agustin": r"C:\Users\user\Documents\Mundial\People/agustin.csv",
    "Alexander": r"C:\Users\user\Documents\Mundial\People/alexander.csv",
    "Cata": r"C:\Users\user\Documents\Mundial\People/cata.csv",
    "Fernando": r"C:\Users\user\Documents\Mundial\People/fernando.csv",
    "Hasan": r"C:\Users\user\Documents\Mundial\People/hasan.csv",
    "Ivan": r"C:\Users\user\Documents\Mundial\People/ivan.csv",
    "Kavi K": r"C:\Users\user\Documents\Mundial\People/kavi_k.csv",
    "Luiza": r"C:\Users\user\Documents\Mundial\People/luiza.csv",
    "Jaco": r"C:\Users\user\Documents\Mundial\People/jaco.csv",
    "Pablo B": r"C:\Users\user\Documents\Mundial\People/pablo_b.csv",
    "Pablo T": r"C:\Users\user\Documents\Mundial\People/pablo_t.csv",
    "Sofia G": r"C:\Users\user\Documents\Mundial\People/sofia_g.csv",
}


max_score = 0

scores = []

# preprocess true bracket


def pre_process(true):
    with open(true, "r") as file:

        bracket = pd.read_csv(true)
        global cuartos_set
        cuartos_set = set()
        cuartos_set = {
            x.lower().strip() for x in set(bracket.loc[:, "Cuartos"]) if x == x
        }
        global semis_set
        semis_set = {x.lower().strip()
                     for x in set(bracket.loc[:, "Semis"]) if x == x}
        semis_set = set()
        global final_set
        final_set = {x.lower().strip()
                     for x in set(bracket.loc[:, "Final"]) if x == x}
        final_set = set()
        global ganador_set
        ganador_set = {
            x.lower().strip() for x in set(bracket.loc[:, "GANADOR"]) if x == x
        }
        ganador_set = set()
        global tercero_set
        tercero_set = {
            x.lower().strip() for x in set(bracket.loc[:, "3ER PUESTO"]) if x == x
        }
        tercero_set = set()

        # not using so that i can manually manipulate the groups for speculation
        # grupos = [
        #     [x.lower().strip() for x in list(bracket.loc[:4, "Grupo A"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[:4, "Grupo B"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[:4, "Grupo C"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[:4, "Grupo D"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[6:10, "Grupo A"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[6:10, "Grupo B"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[6:10, "Grupo C"]) if x == x],
        #     [x.lower().strip() for x in list(bracket.loc[6:10, "Grupo D"]) if x == x],
        # ]

        global grupos
        grupos = [
            ["holanda", "senegal", "ecuador", "qatar"],
            ["inglaterra", "eeuu", "iran", "gales"],
            ["argentina", "polonia", "mexico", "arabia saudi"],
            ["francia", "australia", "tunez", "dinamarca"],
            ["japon", "espana", "alemania", "costa rica"],
            ["marruecos", "croacia", "belgica", "canada"],
            ["brasil", "suiza", "camerun", "serbia"],
            ["portugal", "korea", "uruguay", "ghana"],
        ]

        global octavos
        octavos = set()
        for i in grupos:
            octavos.add(i[0])
            octavos.add(i[1])

    global tournament_stage
    tournament_stage = 0
    # 0->grupos, 1->cuartos, 2->semis, 3->final, 4->ganador
    if len(cuartos_set) != 0:
        tournament_stage += 1
        if len(semis_set) != 0:
            tournament_stage += 1
            if len(final_set) != 0:
                tournament_stage += 1
                if len(ganador_set) != 0:
                    tournament_stage += 1
    return cuartos_set, semis_set, final_set, ganador_set, tercero_set, grupos


persons = ["Maximum Points Possible",
           "Allen",
           "Agustin",
           "Alexander",
           "Cata",
           "Fernando",
           "Hasan",
           "Ivan",
           "Kavi K",
           "Luiza",
           "Jaco",
           "Pablo B",
           "Pablo T",
           "Sofia G"]


def ind_preprocess(person_to_file):
    person_to_bracket = {}
    for person in persons:

        # get person's brackeet and seperate into groups
        with open(person_to_file[person], "r") as _:
            bracket = pd.read_csv(person_to_file[person])
            ind_cuartos_set = {
                x.lower().strip() for x in set(bracket.loc[:, "Cuartos"]) if x == x
            }
            ind_semis_set = {
                x.lower().strip() for x in set(bracket.loc[:, "Semis"]) if x == x
            }
            ind_final_set = {
                x.lower().strip() for x in set(bracket.loc[:, "Final"]) if x == x
            }

            ind_ganador_set = {
                x.lower().strip() for x in set(bracket.loc[:,   "GANADOR"]) if x == x
            }

            ind_tercero_set = {
                x.lower().strip() for x in set(bracket.loc[:, "3ER PUESTO"]) if x == x
            }

            ind_grupos = [
                [x.lower().strip()
                 for x in list(bracket.loc[:4, "Grupo A"]) if x == x],
                [x.lower().strip()
                 for x in list(bracket.loc[:4, "Grupo B"]) if x == x],
                [x.lower().strip()
                 for x in list(bracket.loc[:4, "Grupo C"]) if x == x],
                [x.lower().strip()
                 for x in list(bracket.loc[:4, "Grupo D"]) if x == x],
                [
                    x.lower().strip()
                    for x in list(bracket.loc[6:10, "Grupo A"])
                    if x == x
                ],
                [
                    x.lower().strip()
                    for x in list(bracket.loc[6:10, "Grupo B"])
                    if x == x
                ],
                [
                    x.lower().strip()
                    for x in list(bracket.loc[6:10, "Grupo C"])
                    if x == x
                ],
                [
                    x.lower().strip()
                    for x in list(bracket.loc[6:10, "Grupo D"])
                    if x == x
                ],
            ]

            person_to_bracket[person] = (
                ind_grupos, ind_cuartos_set, ind_semis_set, ind_final_set, ind_ganador_set, ind_tercero_set)
    return person_to_bracket


person_to_bracket = ind_preprocess(person_to_file)


def iterate_to_scores(cuartos1, semis1, final1, ganador1, tercero1, grupo1, person_to_bracket, want_pp):
    scores = []
    true = [grupo1, cuartos1, semis1, final1, ganador1, tercero1]

    for person in person_to_file.keys():
        score = 0
        # group stage scoring
        ind_grupos, ind_cuartos_set, ind_semis_set, ind_final_set, ind_ganador_set, ind_tercero_set = person_to_bracket.get(
            person)
        for ind in range(len(ind_grupos)):
            score += (
                5
                if ind_grupos[ind][0] == grupo1[ind][0]
                else 2
                if ind_grupos[ind][0] == grupo1[ind][1]
                else 0
            )
            score += (
                5
                if ind_grupos[ind][1] == grupo1[ind][1]
                else 2
                if ind_grupos[ind][1] == grupo1[ind][0]
                else 0
            )
            score += 1 if ind_grupos[ind][2] == grupo1[ind][2] else 0
            score += 1 if ind_grupos[ind][3] == grupo1[ind][3] else 0

        # knockout round scoring
        rounds = [
            ind_grupos,
            ind_cuartos_set,
            ind_semis_set,
            ind_final_set,
            ind_ganador_set,
            ind_tercero_set,
        ]

        has_reached_reality = False
        alive = set()
        points_possible = 0
        # 0->grupos, 1->cuartos, 2->semis, 3->final, 4->ganador
        # opting for this to calculate points possible
        for round_counter, round in enumerate(rounds):
            if round_counter > 0:
                if round_counter != 5:
                    score += (2 ** (round_counter - 1) * 6) * len(
                        true[round_counter].intersection(rounds[round_counter])
                    )
                    if(want_pp):
                        if has_reached_reality:
                            points_possible += (2 ** (round_counter - 1) * 6) * len(
                                alive.intersection(rounds[round_counter])
                            )
                else:
                    score += (12) * len(
                        true[round_counter].intersection(rounds[round_counter])
                    )
                    if (want_pp):
                        if has_reached_reality:
                            points_possible += (12) * len(
                                alive.intersection(rounds[round_counter])
                            )
            if want_pp:
                if round_counter == tournament_stage:
                    points_possible = score
                    has_reached_reality = True
                    if round_counter != 0:
                        alive = rounds[round_counter].intersection(
                            true[round_counter])
                    else:
                        for ind_grupo in ind_grupos:
                            alive.add(ind_grupo[0])
                            alive.add(ind_grupo[1])
                        alive = alive.intersection(octavos)

        # easier way to look at what is happening in the above for loop:
        # score += 6 * len(cuartos.intersection(ind_cuartos_set))
        # score += 12 * len(semis.intersection(ind_semis_set))
        # score += 24 * len(final.intersection(ind_final_set))
        # score += 48 * len(ganador.intersection(ind_ganador_set))
        # score += 12 * len(tercero.intersection(ind_tercero_set))

        # string manipulation for table
        if person == "Maximum Points Possible":
            global max_score
            max_score = score
            # print(f"\n {person}: {score}")
            # print('-'*32)
        else:
            if score > points_possible:
                points_possible = score
            scores.append(
                ((person + ":" + ((24 - len(person)) * " ")), score, points_possible)
            )
    return scores


def permuterest(cuartos, semis, final, ganador, tercero, test_grupo):

    person_to_first = {}
    person_to_last = {}

    count = 0

    orig = [[test_grupo[0][0], test_grupo[1][1]], [test_grupo[2][0], test_grupo[3][1]], [test_grupo[4][0], test_grupo[5][1]], [test_grupo[6][0], test_grupo[7][1]], [
        test_grupo[1][0], test_grupo[0][1]], [test_grupo[3][0], test_grupo[2][1]], [test_grupo[5][0], test_grupo[4][1]], [test_grupo[7][0], test_grupo[6][1]]]

    # messy code but converts the current number of permutation for each 'stage' to its binary representation
    # so that it's easier to choose the winners of those games that correspond to that specific permutation
    cuartos_li = []
    for n in range(2 ** (len(orig))):
        l = list(bin(n))[2:]
        if len(l) < 8:
            l = ([0] * (8 - len(l))) + l
        l = [int(x) for x in l]
        for nn in range(len(orig)):
            if nn % 2 == 0:
                cuartos_li.append([orig[nn][l[nn]]])
            else:
                cuartos_li[nn // 2].append((orig[nn][l[nn]]))
        cua_set = set(
            [item for innerlist in cuartos_li for item in innerlist])

        semis_li = []
        for n1 in range(2 ** (len(cuartos_li))):
            ll = list(bin(n1))[2:]
            if len(ll) < 4:
                ll = ([0] * (4 - len(ll))) + ll
            ll = [int(x) for x in ll]
            for nnn in range(len(cuartos_li)):
                if nnn % 2 == 0:
                    semis_li.append([cuartos_li[nnn][ll[nnn]]])
                else:
                    semis_li[nnn // 2].append((cuartos_li[nnn][ll[nnn]]))

            sem_set = set(
                [item for innerlist in semis_li for item in innerlist])
            finals_li = []
            for n2 in range(2 ** (len(semis_li))):
                lll = list(bin(n2))[2:]
                if len(lll) < 2:
                    lll = ([0] * (2 - len(lll))) + lll
                lll = [int(x) for x in lll]
                for nnnn in range(len(semis_li)):
                    if nnnn % 2 == 0:
                        finals_li.append([semis_li[nnnn][lll[nnnn]]])
                    else:
                        finals_li[nnnn //
                                  2].append((semis_li[nnnn][lll[nnnn]]))
                fin_set = set(
                    [item for innerlist in finals_li for item in innerlist])

                for finalist in fin_set:

                    gan_set = {finalist}

                    for third in sem_set.difference(fin_set):

                        thr_set = {third}
                        if (len(cua_set) > 0):
                            count += 1
                            scr = iterate_to_scores(cua_set, sem_set, fin_set,
                                                    gan_set, thr_set, test_grupo, person_to_bracket, False)

                            scr.sort(key=operator.itemgetter(
                                1), reverse=True)
                            first = scr[0]
                            last = scr[-1]

                            if first[0] not in person_to_first:
                                person_to_first[first[0]] = 1
                            else:
                                person_to_first[first[0]] += 1

                            if last[0] not in person_to_last:
                                person_to_last[last[0]] = 1
                            else:
                                person_to_last[last[0]] += 1

                        # redundant after group stage is over since number of permutations possible drops by a factor of 24**(number of groups remaining)
                        if count % 100000 == 0 and count > 0:
                            print(count)
                            print("--- %s seconds ---" %
                                  (time.time() - start_time))

                finals_li.clear()
            semis_li.clear()
        cuartos_li.clear()
    return count, person_to_first, person_to_last


oct_probs = [[0.64, 0.36], [0.88, 0.12], [0.4, 0.6], [0.8, 0.2],
             [0.75, 0.25], [0.82, 0.18], [0.26, 0.74], [0.67, 0.33]]


def permute_with_prob(cuartos, semis, final, ganador, tercero, test_grupo):

    person_to_first = {}
    person_to_last = {}
    total_prob = 0
    count = 0

    orig = [[test_grupo[0][0], test_grupo[1][1]], [test_grupo[2][0], test_grupo[3][1]], [test_grupo[4][0], test_grupo[5][1]], [test_grupo[6][0], test_grupo[7][1]], [
        test_grupo[1][0], test_grupo[0][1]], [test_grupo[3][0], test_grupo[2][1]], [test_grupo[5][0], test_grupo[4][1]], [test_grupo[7][0], test_grupo[6][1]]]
    cuartos_li = []
    for n in range(2 ** (len(orig))):
        prob = 1
        l = list(bin(n))[2:]
        if len(l) < 8:
            l = ([0] * (8 - len(l))) + l
        l = [int(x) for x in l]

        for index in range(len(l)):
            prob *= oct_probs[index][l[index]]

        for nn in range(len(orig)):
            if nn % 2 == 0:
                cuartos_li.append([orig[nn][l[nn]]])
            else:
                cuartos_li[nn // 2].append((orig[nn][l[nn]]))
        cua_set = set(
            [item for innerlist in cuartos_li for item in innerlist])

        semis_li = []
        for n1 in range(2 ** (len(cuartos_li))):
            ll = list(bin(n1))[2:]
            if len(ll) < 4:
                ll = ([0] * (4 - len(ll))) + ll
            ll = [int(x) for x in ll]
            for nnn in range(len(cuartos_li)):
                if nnn % 2 == 0:
                    semis_li.append([cuartos_li[nnn][ll[nnn]]])
                else:
                    semis_li[nnn // 2].append((cuartos_li[nnn][ll[nnn]]))

            sem_set = set(
                [item for innerlist in semis_li for item in innerlist])
            finals_li = []
            for n2 in range(2 ** (len(semis_li))):
                lll = list(bin(n2))[2:]
                if len(lll) < 2:
                    lll = ([0] * (2 - len(lll))) + lll
                lll = [int(x) for x in lll]
                for nnnn in range(len(semis_li)):
                    if nnnn % 2 == 0:
                        finals_li.append([semis_li[nnnn][lll[nnnn]]])
                    else:
                        finals_li[nnnn //
                                  2].append((semis_li[nnnn][lll[nnnn]]))
                fin_set = set(
                    [item for innerlist in finals_li for item in innerlist])

                for finalist in fin_set:
                    gan_set = {finalist}

                    for third in sem_set.difference(fin_set):

                        thr_set = {third}
                        if (len(cua_set) > 0):
                            count += 1
                            total_prob += prob/256

                            scr = iterate_to_scores(cua_set, sem_set, fin_set,
                                                    gan_set, thr_set, test_grupo, person_to_bracket, False)

                            scr.sort(key=operator.itemgetter(
                                1), reverse=True)
                            first = scr[0]
                            last = scr[-1]

                            if first[0] not in person_to_first:
                                person_to_first[first[0]] = prob/256
                            else:
                                person_to_first[first[0]] += prob/256

                            if last[0] not in person_to_last:
                                person_to_last[last[0]] = prob/256
                            else:
                                person_to_last[last[0]] += prob/256

                        # redundant after group stage is over since number of permutations possible drops by a factor of 24**(number of groups remaining)
                        if count % 100000 == 0 and count > 0:
                            print(count)
                            print("--- %s seconds ---" %
                                  (time.time() - start_time))

                finals_li.clear()
            semis_li.clear()
        cuartos_li.clear()
    return total_prob, person_to_first, person_to_last


# most similar and least similar brackets
def bracket_similarity():
    print("Total Sum of Points if this person's bracket is used as the 'true' bracket:")
    for people in person_to_file.keys():
        (
            cuartos_set,
            semis_set,
            final_set,
            ganador_set,
            tercero_set,
            grupos,
        ) = pre_process(person_to_file[people])
        scor = iterate_to_scores(
            cuartos_set, semis_set, final_set, ganador_set, tercero_set, grupos, person_to_bracket, False
        )
        total = 0
        for score in scor:
            total += score[1]
        print(people, ':', total)


cuartos_set, semis_set, final_set, ganador_set, tercero_set, grupos = pre_process(
    true_bracket
)

scores = iterate_to_scores(cuartos_set, semis_set, final_set,
                           ganador_set, tercero_set, grupos, person_to_bracket, True)


def printpermutes(func):
    print('\n')
    cnt, ptf, ptl = func(cuartos_set, semis_set, final_set,
                         ganador_set, tercero_set, grupos)

    if func == permuterest:
        print(f"Total Permutations: {cnt}\n")
        print("Occurrences coming in first:")
        for first in ptf.items():
            print(
                f"{first[0].split(':')[0]}:{' ' * (11- len(first[0].split(':')[0]))}{first[1]}{' '* (8-len(str(first[1])))}=   {round(100*(first[1]/cnt), 3)}%")
        print("\nOccurences coming in last:")
        for first in ptl.items():
            print(
                f"{first[0].split(':')[0]}:{' ' * (11- len(first[0].split(':')[0]))}{first[1]}{' '* (8-len(str(first[1])))}=   {round(100*(first[1]/cnt), 3)}%")

    elif func == permute_with_prob:
        print(
            "Occurrences coming in first with Round of 16 Probabilities taken into account:")
        for first in ptf.items():
            print(
                f"{first[0].split(':')[0]}:{' ' * (11- len(first[0].split(':')[0]))}{round(100*(first[1]/cnt), 3)}%")
        print("\nOccurences coming in last:")
        for first in ptl.items():
            print(
                f"{first[0].split(':')[0]}:{' ' * (11- len(first[0].split(':')[0]))}{round(100*(first[1]/cnt), 3)}%")


bracket_similarity()
printpermutes(permuterest)
printpermutes(permute_with_prob)

# double check slicing of csv's
players = len(scores)
if len(person_to_file.keys()) - 1 != players:
    raise Exception("score-building has failed")


print(f"\n Maximum PP @ Current Round: {max_score}")
print("-" * 42)
print(f" Person{' '*18}Score{' '*6}PP")
print("-" * 42)

# finalize scoreboard
scores.sort(key=operator.itemgetter(1), reverse=True)
for ind, name_score in enumerate(scores):
    if ind == 0:
        print(
            f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} {name_score[0]}{name_score[1]}{' '* (10-len(str(name_score[1])))}{name_score[2]}{' '* (5-len(str(name_score[2])))}{Style.RESET_ALL}"
        )
    elif ind == players - 1:
        print(
            f"{Back.RED}{Style.DIM} {name_score[0]}{name_score[1]}{' '* (10-len(str(name_score[1])))}{name_score[2]}{' '* (5-len(str(name_score[2])))}{Style.RESET_ALL}"
        )
    elif ind > players - 4:
        print(
            f"{Back.YELLOW}{Style.DIM} {name_score[0]}{name_score[1]}{' '* (10-len(str(name_score[1])))}{name_score[2]}{' '* (5-len(str(name_score[2])))}{Style.RESET_ALL}"
        )
    elif ind < 3:
        print(
            f"{Back.GREEN}{Style.NORMAL} {name_score[0]}{name_score[1]}{' '* (10-len(str(name_score[1])))}{name_score[2]}{' '* (5-len(str(name_score[2])))}{Style.RESET_ALL}"
        )
    else:
        print(
            f"{Back.BLACK}{Style.NORMAL} {name_score[0]}{name_score[1]}{' '* (10-len(str(name_score[1])))}{name_score[2]}{' '* (5-len(str(name_score[2])))}{Style.RESET_ALL}"
        )

print("\n* PP: Points Possible")


print("--- %s seconds ---" % (time.time() - start_time))

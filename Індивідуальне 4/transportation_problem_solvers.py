import numpy as np
from typing import List, Tuple
from copy import deepcopy


class VogelsSolution:
    def __init__(
            self,
            costs: List,
            supply: List,
            demand: List
    ) -> None:
        self.costs: np.array = costs
        self.supply: np.array = supply
        self.demand: np.array = demand
        self._validate()

    def get_diff(self) -> Tuple[np.array, np.array]:
        col_diff, row_diff = [], []

        for row in self.costs:
            min = np.min(row)
            next_min = np.min(row[row != min])
            row_diff.append(next_min - min)

        for col in self.costs.T:
            min = np.min(col)
            next_min = np.min(col[col != min])
            col_diff.append(next_min - min)

        return np.array(row_diff), np.array(col_diff)

    # use this implementation
    # https://www.geeksforgeeks.org/transportation-problem-set-4-vogels-approximation-method/
    def solve(self):
        result = []
        supply_copy = deepcopy(self.supply)
        demand_copy = deepcopy(self.demand)
        cost_copy = deepcopy(self.costs)

        while np.max(supply_copy) != 0 or np.max(demand_copy) != 0:
            row_diff, col_diff = self.get_diff()
            # finding the maxiumum element in row difference array
            max_row_diff = np.max(row_diff)
            # finding the maxiumum element in col difference array
            max_col_diff = np.max(col_diff)

            # if the row diff max element is greater than or equal to col diff max element
            if max_row_diff >= max_col_diff:
                for rind, rval in enumerate(row_diff):
                    if rval == max_row_diff:
                        # finding the minimum element in grid index where the maximum was found in the row difference
                        ming = np.min(cost_copy[rind])
                        for cind, cval in enumerate(cost_copy[rind]):
                            if cval == min:
                                # calculating the min of supply and demand in that row and col
                                mins = np.min(
                                    [supply_copy[rind], demand_copy[cind]])
                                result.append((ming, mins))
                                # subtracting the min from supply and demand
                                supply_copy[rind] -= mins
                                demand_copy[cind] -= mins
                                # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                                if demand_copy[cind] == 0:
                                    cost_copy[:, cind] = np.inf
                                # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                                else:
                                    cost_copy[rind, :] = np.inf
                                break
                        break
            # if the col diff max element is greater than the row diff max element
            else:
                for cind, cval in enumerate(col_diff):
                    if cval == max_col_diff:
                        # finding the minimum element in grid index where the maximum was found in the col difference
                        ming = np.min(cost_copy[:, cind])
                        for rind, rval in enumerate(cost_copy[:, cind]):
                            if rval == ming:
                                # calculating the min of supply and demand in that row and col
                                mins = np.min(
                                    [supply_copy[rind], demand_copy[cind]])
                                result.append((ming, mins))
                                # subtracting the min from supply and demand
                                supply_copy[rind] -= mins
                                demand_copy[cind] -= mins
                                # if demand is smaller then the entire col is assigned max value so that the col is eliminated for the next iteration
                                if demand_copy[cind] == 0:
                                    cost_copy[:, cind] = np.inf
                                # if supply is smaller then the entire row is assigned max value so that the row is eliminated for the next iteration
                                else:
                                    cost_copy[rind, :] = np.inf
                                break
                        break
        return result

    @property
    def costs(self):
        return self._costs

    @costs.setter
    def costs(self, costs: List):
        self._costs = np.array(costs)

    @property
    def supply(self):
        return self._supply

    @supply.setter
    def supply(self, supply: List):
        self._supply = np.array(supply)

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, demand: List):
        self._demand = np.array(demand)

    def _validate(self):
        if self.supply.sum() != self.demand.sum():
            raise ValueError('Supply and demand must be equal')

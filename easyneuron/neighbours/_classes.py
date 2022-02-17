# Copyright 2021 Neuron-AI GitHub Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import annotations

from abc import ABC, abstractmethod
from functools import total_ordering
from typing import Any, Sequence

from easyneuron._classes import Model
from easyneuron.types import X_Data


@total_ordering
class _KNN(Model, ABC):
    __slots__ = "K"
    K: int

    def __lt__(self, other: _KNN) -> Any:
        return self.K < other.K

    @abstractmethod
    def fit(self, X: X_Data, y: Sequence, *args, **kwargs) -> Model:
        ...

    @abstractmethod
    def predict(self, X: X_Data, *args, **kwargs) -> Sequence:
        ...

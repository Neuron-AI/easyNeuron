# Copyright 2022 Neuron-AI GitHub Authors. All Rights Reserved.
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

from typing import Any

from easyneuron._classes import Layer
from numpy import dot, ones, zeros


class Dense(Layer):
    def __init__(
        self, neurons: int, inputs: int = 1, activation: str = "linear"
    ) -> None:
        self.weights = ones((neurons,))
        self.biases = zeros(neurons)
        self.activation = activation

    def forward(self, X) -> Any:
        dot_products = [
            dot(X, neurons_weights) + self.biases[i]
            for i, neurons_weights in enumerate(self.weights)
        ]

        print(dot_products)

    def backward(self, X) -> Any:
        ...

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPD/2lM9zTPN/hJsZbUEEwO"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "A + B   \n",
        "[1000번](https://www.acmicpc.net/problem/1000)"
      ],
      "metadata": {
        "id": "HN7t2ITsT3hd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# solved\n",
        "A, B = map(int, input().split())\n",
        "print(A+B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TCv_TKWdUOhg",
        "outputId": "bf91dfc8-780a-476e-e733-6309fe645907"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2\n",
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "A - B   \n",
        "[1001번](https://www.acmicpc.net/problem/1001)"
      ],
      "metadata": {
        "id": "hWMRCLEGUqaf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# solved\n",
        "A, B = map(int, input().split())\n",
        "print(A-B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3sjJNE6LUrCm",
        "outputId": "e42197c5-c62e-46f2-be71-918020c6dec3"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 2\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "터렛   \n",
        "[1002번](https://www.acmicpc.net/problem/1002)"
      ],
      "metadata": {
        "id": "Eps9tb1gUrFq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# solved\n",
        "def counts(x1, y1, r1, x2, y2, r2):\n",
        "  d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)\n",
        "  if x1 == x2 and y1 == y2:\n",
        "    if r1 == r2:\n",
        "      res.append(-1)\n",
        "    else:\n",
        "      res.append(0)\n",
        "  else:\n",
        "    if d > abs(r1 - r2) and d < abs(r1 + r2):\n",
        "      res.append(2)\n",
        "    elif d == abs(r1 - r2) or d == abs(r1 + r2):\n",
        "      res.append(1)\n",
        "    elif d > abs(r1 + r2):\n",
        "      res.append(0)\n",
        "    elif d< abs(r1 - r2):\n",
        "      res.append(0)\n",
        "    else:\n",
        "      pass\n",
        "res = []\n",
        "for i in range(int(input())):\n",
        "  x1, y1, r1, x2, y2, r2 = map(int, input().split())\n",
        "  counts(x1, y1, r1, x2, y2, r2)\n",
        "for _ in res:\n",
        "  print(_)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S4cdsoOlUrJL",
        "outputId": "84879df0-662e-4da6-ea82-eea621f4caae"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "0 0 13 40 0 37\n",
            "0 0 3 0 7 4\n",
            "1 1 1 1 1 5\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ]
    }
  ]
}
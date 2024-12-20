{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Shankaracharya06/Control_Statements/blob/main/NumpyMethods.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "rRrg2-XLPtlS"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "# import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "DB4Z5EPgPxLa",
        "outputId": "723ecd6c-f6a6-43af-bcf1-e2a956731db7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.26.4\n",
            "[1 4 5 6]\n",
            "[1. 4. 5. 6.]\n",
            "['1' '4' 'hello' '5' '6']\n",
            "[1.+0.j 4.+0.j 8.+0.j 5.+4.j 6.+0.j]\n"
          ]
        }
      ],
      "source": [
        "print((np.__version__))         # 1.26.4 (verison of numpy)\n",
        "\n",
        "# Priority of typcasting during converting into array   ------------->    bool < int < float < complex < str < set < dict\n",
        "\n",
        "list1 = [1, 4, 5, 6]\n",
        "print(np.array(list1))          # [1, 4, 5, 6]\n",
        "\n",
        "list2 = [1, 4.0, 5, 6]\n",
        "print(np.array(list2))          # [1., 4., 5., 6.]\n",
        "\n",
        "list3 = [1, 4, \"hello\", 5, 6]\n",
        "print(np.array(list3))          # ['1' '4' 'hello' '5' '6']\n",
        "\n",
        "list4 = [1, 4,8, 5+4j, 6]\n",
        "print(np.array(list4))          # [1.+0.j 4.+0.j 8.+0.j 5.+4.j 6.+0.j]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "id": "p8imkQzqY-rL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "62471214-e511-4796-db0b-46b8f7705b06"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 5 8 6 9]\n",
            "1\n",
            "int64\n",
            "(5,)\n",
            "<built-in method reshape of numpy.ndarray object at 0x7c4fed720870>\n",
            "[[ 1  2  3]\n",
            " [ 5  8 11]]\n",
            "2\n",
            "int64\n",
            "(2, 3)\n",
            "<built-in method reshape of numpy.ndarray object at 0x7c4fed720c30>\n",
            "[[[1 2 7]\n",
            "  [5 8 3]]\n",
            "\n",
            " [[8 7 5]\n",
            "  [6 3 7]]]\n",
            "3\n",
            "int64\n",
            "(2, 2, 3)\n",
            "<built-in method reshape of numpy.ndarray object at 0x7c4fed722b50>\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([   0,    2,    4,    6,    8,   10,   12,   14,   16,   18,   20,\n",
              "         22,   24,   26,   28,   30,   32,   34,   36,   38,   40,   42,\n",
              "         44,   46,   48,   50,   52,   54,   56,   58,   60,   62,   64,\n",
              "         66,   68,   70,   72,   74,   76,   78,   80,   82,   84,   86,\n",
              "         88,   90,   92,   94,   96,   98,  100,  102,  104,  106,  108,\n",
              "        110,  112,  114,  116,  118,  120,  122,  124,  126,  128,  130,\n",
              "        132,  134,  136,  138,  140,  142,  144,  146,  148,  150,  152,\n",
              "        154,  156,  158,  160,  162,  164,  166,  168,  170,  172,  174,\n",
              "        176,  178,  180,  182,  184,  186,  188,  190,  192,  194,  196,\n",
              "        198,  200,  202,  204,  206,  208,  210,  212,  214,  216,  218,\n",
              "        220,  222,  224,  226,  228,  230,  232,  234,  236,  238,  240,\n",
              "        242,  244,  246,  248,  250,  252,  254,  256,  258,  260,  262,\n",
              "        264,  266,  268,  270,  272,  274,  276,  278,  280,  282,  284,\n",
              "        286,  288,  290,  292,  294,  296,  298,  300,  302,  304,  306,\n",
              "        308,  310,  312,  314,  316,  318,  320,  322,  324,  326,  328,\n",
              "        330,  332,  334,  336,  338,  340,  342,  344,  346,  348,  350,\n",
              "        352,  354,  356,  358,  360,  362,  364,  366,  368,  370,  372,\n",
              "        374,  376,  378,  380,  382,  384,  386,  388,  390,  392,  394,\n",
              "        396,  398,  400,  402,  404,  406,  408,  410,  412,  414,  416,\n",
              "        418,  420,  422,  424,  426,  428,  430,  432,  434,  436,  438,\n",
              "        440,  442,  444,  446,  448,  450,  452,  454,  456,  458,  460,\n",
              "        462,  464,  466,  468,  470,  472,  474,  476,  478,  480,  482,\n",
              "        484,  486,  488,  490,  492,  494,  496,  498,  500,  502,  504,\n",
              "        506,  508,  510,  512,  514,  516,  518,  520,  522,  524,  526,\n",
              "        528,  530,  532,  534,  536,  538,  540,  542,  544,  546,  548,\n",
              "        550,  552,  554,  556,  558,  560,  562,  564,  566,  568,  570,\n",
              "        572,  574,  576,  578,  580,  582,  584,  586,  588,  590,  592,\n",
              "        594,  596,  598,  600,  602,  604,  606,  608,  610,  612,  614,\n",
              "        616,  618,  620,  622,  624,  626,  628,  630,  632,  634,  636,\n",
              "        638,  640,  642,  644,  646,  648,  650,  652,  654,  656,  658,\n",
              "        660,  662,  664,  666,  668,  670,  672,  674,  676,  678,  680,\n",
              "        682,  684,  686,  688,  690,  692,  694,  696,  698,  700,  702,\n",
              "        704,  706,  708,  710,  712,  714,  716,  718,  720,  722,  724,\n",
              "        726,  728,  730,  732,  734,  736,  738,  740,  742,  744,  746,\n",
              "        748,  750,  752,  754,  756,  758,  760,  762,  764,  766,  768,\n",
              "        770,  772,  774,  776,  778,  780,  782,  784,  786,  788,  790,\n",
              "        792,  794,  796,  798,  800,  802,  804,  806,  808,  810,  812,\n",
              "        814,  816,  818,  820,  822,  824,  826,  828,  830,  832,  834,\n",
              "        836,  838,  840,  842,  844,  846,  848,  850,  852,  854,  856,\n",
              "        858,  860,  862,  864,  866,  868,  870,  872,  874,  876,  878,\n",
              "        880,  882,  884,  886,  888,  890,  892,  894,  896,  898,  900,\n",
              "        902,  904,  906,  908,  910,  912,  914,  916,  918,  920,  922,\n",
              "        924,  926,  928,  930,  932,  934,  936,  938,  940,  942,  944,\n",
              "        946,  948,  950,  952,  954,  956,  958,  960,  962,  964,  966,\n",
              "        968,  970,  972,  974,  976,  978,  980,  982,  984,  986,  988,\n",
              "        990,  992,  994,  996,  998, 1000])"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ],
      "source": [
        "arr1D = np.array([1,5,8,6,9])\n",
        "print(arr1D)         # [1 5 8 6 9]\n",
        "print(arr1D.ndim)\n",
        "print(arr1D.dtype)\n",
        "print(arr1D.shape)   # (5,)\n",
        "print(arr1D.reshape)\n",
        "\n",
        "\n",
        "arr2D = np.array([\n",
        "                  [1,2,3],\n",
        "                  [5,8,11]\n",
        "                ])\n",
        "print(arr2D)         # [1 5 8 6 9]\n",
        "print(arr2D.ndim)\n",
        "print(arr2D.dtype)\n",
        "print(arr2D.shape)   # (5,)\n",
        "print(arr2D.reshape)\n",
        "\n",
        "arr3D = np.array([\n",
        "                  [[1,2,7],[5,8,3]],\n",
        "                  [[8,7,5],[6,3,7]]\n",
        "                 ])\n",
        "print(arr3D)         # [1 5 8 6 9]\n",
        "print(arr3D.ndim)\n",
        "print(arr3D.dtype)\n",
        "print(arr3D.shape)   # (5,)\n",
        "print(arr3D.reshape)\n",
        "\n",
        "np.arange(0,1001,2)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_arr = np.linspace(-4,5,50)\n",
        "# print(new_arr)              # [-4.         -3.81632653 -3.63265306 -3.44897959 -3.26530612 -3.08163265\n",
        "                            # -2.89795918 -2.71428571 -2.53061224 -2.34693878 -2.16326531 -1.97959184\n",
        "                            # -1.79591837 -1.6122449  -1.42857143 -1.24489796 -1.06122449 -0.87755102\n",
        "                            # -0.69387755 -0.51020408 -0.32653061 -0.14285714  0.04081633  0.2244898\n",
        "                            #  0.40816327  0.59183673  0.7755102   0.95918367  1.14285714  1.32653061\n",
        "                            #  1.51020408  1.69387755  1.87755102  2.06122449  2.24489796  2.42857143\n",
        "                            #  2.6122449   2.79591837  2.97959184  3.16326531  3.34693878  3.53061224\n",
        "                            #  3.71428571  3.89795918  4.08163265  4.26530612  4.44897959  4.63265306\n",
        "                            #  4.81632653  5.        ]\n",
        "new_arr = np.random.randint(10.5,26.5,50)\n",
        "# print(new_arr)              # [23 16 21 18 18 24 14 23 18 18 12 19 17 14 11 20 21 11 10 10 14 13 14 24\n",
        "                            #  20 25 21 24 16 20 15 17 12 11 14 24 19 17 15 11 11 16 14 15 14 19 15 14\n",
        "                            #  22 11]\n",
        "new_arr = np.random.rand(5)\n",
        "# print(new_arr)              # [0.79332798 0.56400245 0.33369816 0.57638247 0.88839336]\n",
        "\n",
        "new_arr = np.random.randn(20)\n",
        "# print(new_arr)              # [-0.85172822 -0.21545446 -0.78639605  1.63299493  1.73847166]\n",
        "\n",
        "fruits = ['apple','orange','banana','pomogrenate']\n",
        "new_arr = np.random.choice(fruits)\n",
        "# print(new_arr)                # give any random item from the collection(fruits)\n",
        "\n",
        "songs = ['perfect', 'blinding lights', 'night change']\n",
        "np.random.shuffle(songs)\n",
        "# print(songs)                  # it will shuffle the original collection(songs) i.e rearrange the oroginal collection"
      ],
      "metadata": {
        "id": "lyYpLe0MZ6HM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c8b47272-4d46-4ec9-d356-0fa99704de2d"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "apple\n",
            "['night change', 'blinding lights', 'perfect']\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO6GEzVr2SvK1YeE9mNHLlC",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
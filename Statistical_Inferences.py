import numpy as np
import scipy.stats as st


def mean(array):
    """
    Computes mean
    """
    length = len(array)
    sum = 0
    for i in range(length):
        sum+=array[i]
    mean = sum/length
    return mean


def median (array):
    """
    Computes median of a given numeric array
    """
    num_elements = len(array)
    array_sorted = sorted(array)
    if num_elements%2==1:
        median = array_sorted[int(((num_elements+1)/2)-1)]
    else:
        median = (array_sorted[int(((num_elements+1)/2)-1)]+array_sorted[int(((num_elements+1)/2))])/2.0
    return median


def variance(array):
    """
    Computes variance
    """
    length = len(array)
    avg = mean(array)
    sumsq = 0
    for i in range(length):
        sumsq+=(array[i]-avg)**2
    variance = sumsq/length
    return variance


def Summary(array):
    array = np.array(array)
    sorted_array = sorted(array)
    print(array)

    # Using np.amax()
    print("Max of the array:",np.amax(array))
    # Using array.max()
    print("Max of the array:",array.max())

    # Using np.amin()
    print("Min of the array:",np.amin(array))
    # Using array.max()
    print("Min of the array:",array.min())

    # Compute range by using max() and min() functions
    print("Range of the array: ", array.max()-array.min())
    # Compute range by using ptp() function
    print("Range of the array: ", np.ptp(array))

    # Percentile
    print("20th percentile of the array: ", np.percentile(array,20))

    # Quantile
    print("0.25-th quantile of the array: ", np.quantile(array,0.25))
    print("0.5-th quantile of the array: ", np.quantile(array,0.5))
    print("0.75-th quantile of the array: ", np.quantile(array,0.75))

    #Mean
    print("Mean: ", array.mean())

    # Median
    print("Median", median(array))
    print("Median", np.median(np.array(array)))

    print("Variance", array.var())
    print("SD", array.std())

    print("Mean ignoring NaN:", np.nanmean(array))
    print("Var ignoring NaN:", np.nanvar(array))
    print("Std. dev ignoring NaN:", np.nanstd(array))
    print("Median ignoring NaN:", np.nanmedian(array))


def multi_anova(groups, alpha=0.05):
    """
    Two-way ANOVA between multiple groups
    groups: A dictionary object of trial groups
    """
    from itertools import combinations
    list_anova = list(combinations(list(groups.keys()), 2))

    for comb in list_anova:
        _, p = st.f_oneway(groups[comb[0]], groups[comb[1]])
        if p > 0.05:
            print("\nANOVA fails to reject the hypothesis of equal mean for {} and {}".format(comb[0], comb[1]))
        else:
            print("\nWe reject the hypothesis of equal mean for {} and {} as per ANOVA test result".format(comb[0],
                                                                                                           comb[1]))


def independent_ttest(data1, data2, alpha=0.05):
    """
    Student's t-test for independent groups

    Argument:
        data1: First group data in numpy array format
        data2: Second group two data in numpy array format
        alpha: Significance level

    Returns:
        t_stat: Computed t-statistic
        df: Degrees of freedom
        cv: Critical value
        p: p-value (of NULL hypothesis)
    """
    import scipy.stats as st
    # calculate means
    mean1, mean2 = np.mean(data1), np.mean(data2)
    # calculate standard errors
    se1, se2 = st.sem(data1), st.sem(data2)
    # standard error on the difference between the samples
    sed = np.sqrt(se1 ** 2.0 + se2 ** 2.0)
    # calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    # degrees of freedom
    df = len(data1) + len(data2) - 2
    # calculate the critical value
    cv = st.t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - st.t.cdf(abs(t_stat), df)) * 2.0
    # return everything
    return t_stat, df, cv, p
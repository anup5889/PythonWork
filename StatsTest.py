PeopleWhoInteractMore=JoinedInteractionPerformance[JoinedInteractionPerformance['ACSD']> \
                                                   JoinedInteractionPerformance.ACSD.mean()]
PeopleWhoInteractLess=JoinedInteractionPerformance[JoinedInteractionPerformance['ACSD']< \
                                                   JoinedInteractionPerformance.ACSD.mean()]


result=scipy.stats.ttest_ind(PeopleWhoInteractMore['score'], PeopleWhoInteractLess['score'], equal_var=False)
print result

result2=scipy.stats.ranksums(PeopleWhoInteractMore['score'], PeopleWhoInteractLess['score'])
print result2

result3=scipy.stats.mannwhitneyu(PeopleWhoInteractMore['score'], PeopleWhoInteractLess['score'])
print result3


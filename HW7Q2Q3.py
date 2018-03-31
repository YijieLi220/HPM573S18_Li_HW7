##Q2
print("The number of participants that survived beyond 5 years in a cohort of 𝑁 participants will follow Bernoulli (binomial) distribution.")
print("The parameter (probability of a random event) is q.")


##Q3
import scipy.stats as Stat

percentage = 0.5
k=400
n=573
weight=Stat.binom.pmf(k=k,n=n,p=percentage)
print(weight)
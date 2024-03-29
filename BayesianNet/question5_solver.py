class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
        #print ('_________NEW________')
        pr_max = -999999
        final_letter = '0'
        query = '``'+query+'``'
        #print(query)
        for x in self.letters:
            this_query = query.replace('_',x)
            #print ('Current Guess Letter :', x)
            count = 0
            pr_prod = 1
            for i in this_query:
                #print ('Current query letter :', i)
                count += 1
                if count == 1: pr_prod = pr_prod * 1
                #elif count == len(query):
                    #pr_prod = pr_prod * 1
                elif count == 2: pr_prod = pr_prod * 1
                else :
                    #print('PR(', i, ',', this_query[count-3], ',', this_query[count-2], ',)=', self.cpt2.conditional_prob(i, this_query[count-3],this_query[count-2]))
                    pr_prod = pr_prod * self.cpt2.conditional_prob(i, this_query[count-3],this_query[count-2])
            #print('pr_prod for', x, '=', pr_prod)
            if pr_prod > pr_max:
                pr_max = pr_prod
                final_letter = x
        #print('-----for query=',query, 'best match was', final_letter, 'with prob', pr_max)
        return final_letter


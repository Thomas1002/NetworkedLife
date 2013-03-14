R = mcat([5, 0, 5, 4, OMPCSEMI, 0, 1, 1, 4, OMPCSEMI, 4, 1, 2, 4, OMPCSEMI, 3, 4, 0, 3, OMPCSEMI, 1, 5, 3, 0])
#% Problem 4.1 %%
[num_users, num_movies] = size(R)

num_ratings = nnz(R)
r_avg = sum(R(mslice[:])) / num_ratings
[x, y] = find(R)
A = zeros(num_ratings, num_movies + num_users)
temp = size(x)
for i in mslice[1:temp]:
    A(i, x(i)).lvalue = 1
    A(i, num_users + y(i)).lvalue = 1
    end
    Rt = R
    Rt(Rt == 0).lvalue = mcat([])
    c = Rt(mslice[:]) - r_avg
    b = pinv(A) * c
    bu = b(mslice[1:num_users])
    bi = b(mslice[num_users + 1:end]).cT
    R_baseline = bu(mslice[:], ones(1, num_movies)) + bi(ones(1, num_users), mslice[:]) + r_avg
    R_baseline(R_baseline > 5).lvalue = 5
    R_baseline(R_baseline < 1).lvalue = 1
    #% Problem 4.2 %%
    R_tilde = (R - R_baseline) *elmul* (R > 0)
    D = zeros(num_movies, num_movies)
    for i in mslice[1:num_movies]:
        for j in mslice[1:num_movies]:
            idx = logical_and(R(mslice[:], i) > 0, R(mslice[:], j) > 0)
            vi = R_tilde(idx, i)
            vj = R_tilde(idx, j)
            D(i, j).lvalue = sum(vi *elmul* vj) / sqrt(sum(vi *elmul* vi) * sum(vj *elmul* vj))
            end
            end
            R_neighborhood = zeros(num_users, num_movies)
            k = 2        # pick 2 top neighbors
            for j in mslice[1:num_movies]:
                [val_sort, idx_sort] = sort(abs(D(j, mslice[:])), mstring('descend'))
                idx = idx_sort(mslice[1:k + 1])            # must include self movie in idx_sort
                idx(idx == j).lvalue = mcat([])            # remove self movie
                for i in mslice[1:num_users]:
                    idx2 = idx
                    idx2(R(i, idx2) == 0).lvalue = mcat([])
                    if (length(idx2) > 0):
                        R_neighborhood(i, j).lvalue = sum(D(j, idx2) *elmul* R_tilde(i, idx2)) / sum(abs(D(j, idx2)))
                        end
                        end
                        end
                        R_neighborhood = R_baseline + R_neighborhood
                        R_neighborhood(R_neighborhood > 5).lvalue = 5
                        R_neighborhood(R_neighborhood < 1).lvalue = 1
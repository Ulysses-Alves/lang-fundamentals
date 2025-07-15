
function fibo(n)
    if n == 0
        return 0
    elseif n == 1
        return 1
    else
        return fibo(n - 1) + fibo(n - 2)
    end
end

# Notes
# REMEBER THAT JULIA HAS 1-BASED INDEXING
# vectors and arrays are the same thing here

function fiboM(n, memo::Vector{Int} = fill(-1, n + 1))

    if memo[n + 1] != -1
        return memo[n + 1]
    elseif n == 0
        return memo[n + 1] = 0
    elseif n == 1
        return memo[n + 1] = 1
    else
        memo[n + 1] = fiboM(n - 1, memo) + fiboM(n - 2, memo)
    end
    return memo[n + 1]
end

println(fiboM(7))
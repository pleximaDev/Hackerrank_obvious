// in progress
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the arrayManipulation function below.
long arrayManipulation(int n, vector<vector<int>> queries) 
{
    // int arr[n] = {0};
    // long long *arr = malloc(n * sizeof(long long));
    std::vector<int> arr(n);
    // memset(arr, 0, sizeof(*arr));
    // memset(arr, 0, n * sizeof(long long));
    arr.assign(n, 0);

    cout << "que == " << queries[0][2] << endl;
    cout << "size == " << queries.size() << endl;

    // for(std::vector<int>::iterator it = arr.begin(); it != arr.end(); ++it)
    // {
    //     it->doSomething();
    // }

    int len = queries.size();
    for(int i = 0; i < len; i++)
    {
        std::for_each(arr.begin() + queries[i][0], arr.end() - queries[i][1], [](double& d) { d += queries[i][2];});
        /*
        for(long long j = queries[i][0]; j <= queries[i][1]; j++)
        {
            // printf("from %d to %d\n", *(*(queries + i) + 0), *(*(queries + i) + 1));
            // printf("add %d to arr[%d]\n", *(*(queries + i) + 2), j);
            arr[j - 1] += queries[i][2];
        }
        */
        // for(int l = 0; l < n; l++)
        // {
        //     printf("arr[%d] = %d\n", l, *(arr + l));
        // }
        // printf("\n");
    }
    // printf("n == %d\n", n);
    // printf("q_r == %d\n", queries_rows);
    // printf("q_c == %d\n", queries_columns);
    // printf("que == %d\n", *(*(queries + 2) + 0));

    // for(int i = 0; i < n; i++)
    // {
    //     printf("arr[%d] = %d\n", i, arr[i]);
    // }

    long long max = 0;
    for(long long i = 0; i < n; i++)
    {
        if (arr[i] > max) max = arr[i];
        // printf("arr[%d] = %d\n", i, arr[i]);
    }

    // *(*(queries + 2) + 0)   *(*(queries + rows) + columns)
    return max;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    vector<vector<int>> queries(m);
    for (int i = 0; i < m; i++) {
        queries[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> queries[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    long result = arrayManipulation(n, queries);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}


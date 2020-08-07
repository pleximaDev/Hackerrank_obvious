#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);



int main()
{
    string nd_temp;
    getline(cin, nd_temp);

    vector<string> nd = split_string(nd_temp);

    int n = stoi(nd[0]);

    int d = stoi(nd[1]);

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    // Works for cpp but runtime error for pure c
    for(int i = d % n; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    for(int i = 0; i < d % n; i++)
    {
        printf("%d ", a[i]);
    }


    /////////////////////  Shortest way /////////////////////
    // (Works, but occurs error with testcase #1) c vers.
    // for(int i = d % n; i < n; i++)
    // {
    //     printf("%d ", a[i]);
    // }
    // for(int i = 0; i < d % n; i++)
    // {
    //     printf("%d ", a[i]);
    // }
    /////////////////////////////////////////////////////////




    /////////////////////////////////////////////////////////////
    // Works, but failes one testcase cause strange runtime error
    //  c vers.
    // int loops;
    // if (d > n - 1)
    // {
    //     loops = d % n;
    // }
    // else 
    // {
    //     loops = d;
    // }
    // // printf("Loops == %d\n", loops);
    
    // int* temp = malloc(n * sizeof(int));
    // *(temp + 0) = *(a + loops);
    // int j = loops + 1;
    // for(int i = 1; i < n; i++)
    // {
    //     if(j >= n){j = 0;}
    //     *(temp + i) = *(a + j);
    //     j++;
    // }
    // for(int i=0; i < n; i++) 
    // {
    //     printf("%d ", temp[i]);
    // }
    /////////////////////////////////////////////////////////////

    ////////////////////////////////////////////////////////
    // int* temp = malloc(n * sizeof(int));
    // for(int i=0; i < d; i++)
    // {
    //     *(temp + n - 1) = *(a + 0);
    //     for(int j=0; j < n - 1; j++)
    //     {
    //         *(temp + j) = *(a + j + 1);
    //     }
    //     a = temp;
    //     for(int l=0; l < n /*(sizeof(a)/sizeof(a[0]))*/; l++) 
    //     {
    //         printf("%d ", a[l]);
    //     }
    //     printf("\n");
    // }
    // for(int i=0; i < n /*(sizeof(a)/sizeof(a[0]))*/; i++) 
    // {
    //     printf("%d ", a[i]);
    // }
    ////////////////////////////////////////////////////////

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


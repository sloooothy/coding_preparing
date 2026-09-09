class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // 【提示 1：宣告 Priority Queue】
        // C++ 預設是 Max Heap，會把「最大值」放在頂端 (pq.top())。
        // 我們儲存 Pair 結構：<距離平方, 點的座標> -> pair<int, vector<int>>
        // 宣告方法: priority_queue<pair<int, vector<int>>> pq;
        priority_queue<pair<int, vector<int>>> pq;

        vector<vector<int>> res;

        // 步驟一：遍歷每一個點
        for(int i = 0; i < points.size(); i++)
        {
            // 1. 計算當前點到原點的歐幾里得距離平方 (x^2 + y^2)
            // （不需要開開根號 sqrt，因為平方大小關係是一樣的，開根號會變成浮點數）
            int x=points[i][0];
            int y=points[i][1];
            int dist=x*x+y*y;

            //cout<<x<<endl;
            //cout<<y<<endl;
            
            // 【提示 2：將資料推入 Priority Queue】
            // pq.push({dist, points[i]});
            pq.push({dist, points[i]});
            //cout<<pq.top().first<<endl;

            // 【提示 3：維護 Heap 的大小永遠不超過 k】
            // 如果 pq.size() > k：
            // 代表目前 Heap 裡的點太多了，把「距離最遠（也就是頂端）」的那個點彈出！
            // pq.pop();
            if(pq.size() > k)
            {
                pq.pop();
            }
        }

        // 步驟二：此時 Priority Queue 裡面留下來的就是「前 K 個最近的點」
        // 使用迴圈把 pq 裡面的點取出，放到 res 陣列中
        while(!pq.empty()) {
            // 【提示 4：取出頂端元素並放入 res】
            // res.push_back(pq.top().second); // pq.top().second 就是當前點的座標 vector<int>
            // pq.pop(); // 記得彈出已處理的元素
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};

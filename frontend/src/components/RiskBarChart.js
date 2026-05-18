import {

  BarChart,

  Bar,

  XAxis,

  YAxis,

  CartesianGrid,

  Tooltip,

  ResponsiveContainer

} from "recharts";


function RiskBarChart() {

  const data = [

    {
      risk: "Low",
      count: 700
    },

    {
      risk: "Medium",
      count: 200
    },

    {
      risk: "High",
      count: 100
    }
  ];


  return (

    <div className="bg-white p-6 rounded-2xl shadow-lg">

      <h2 className="text-2xl font-bold mb-6">

        Risk Distribution

      </h2>


      <div className="h-80">

        <ResponsiveContainer>

          <BarChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="risk" />

            <YAxis />

            <Tooltip />

            <Bar

              dataKey="count"

              fill="#2563EB"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default RiskBarChart;
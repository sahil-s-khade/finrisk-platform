import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

function FraudAnalytics() {

  return (

    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-6 lg:p-8 max-w-[1600px] mx-auto">

          {/* HEADER */}

          <div className="mb-10">

            <h1 className="text-5xl font-extrabold text-gray-800 mb-4">

              Fraud Analytics Center

            </h1>

            <p className="text-gray-600 text-lg">

              AI-powered fraud intelligence,
              predictive analytics,
              and enterprise transaction insights.

            </p>

          </div>



          {/* TOP ANALYTICS CARDS */}

          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">

            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                Fraud Growth

              </div>

              <div className="text-5xl font-bold text-red-500">

                +18%

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                AI Risk Score

              </div>

              <div className="text-5xl font-bold text-orange-500">

                92

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                Detection Accuracy

              </div>

              <div className="text-5xl font-bold text-green-600">

                98%

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                AI Prediction Rate

              </div>

              <div className="text-5xl font-bold text-blue-600">

                96%

              </div>

            </div>

          </div>



          {/* FRAUD INSIGHTS */}

          <div className="bg-white rounded-3xl shadow-lg p-8 mb-10">

            <div className="flex items-center justify-between mb-8">

              <h2 className="text-3xl font-bold">

                Executive Fraud Insights

              </h2>

              <div className="text-red-500 font-bold">

                ● LIVE ANALYTICS

              </div>

            </div>


            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

              {/* BOX */}

              <div className="bg-red-50 rounded-2xl p-6">

                <div className="text-4xl mb-4">

                  🚨

                </div>

                <div className="text-2xl font-bold text-red-600 mb-3">

                  High Risk Transactions

                </div>

                <p className="text-gray-600 leading-7">

                  AI models detected increased
                  fraudulent transaction spikes
                  across high-value transfers.

                </p>

              </div>



              {/* BOX */}

              <div className="bg-blue-50 rounded-2xl p-6">

                <div className="text-4xl mb-4">

                  🤖

                </div>

                <div className="text-2xl font-bold text-blue-600 mb-3">

                  ML Prediction Engine

                </div>

                <p className="text-gray-600 leading-7">

                  Real-time machine learning
                  scoring systems continue
                  to classify suspicious activities.

                </p>

              </div>



              {/* BOX */}

              <div className="bg-green-50 rounded-2xl p-6">

                <div className="text-4xl mb-4">

                  📊

                </div>

                <div className="text-2xl font-bold text-green-600 mb-3">

                  Risk Intelligence

                </div>

                <p className="text-gray-600 leading-7">

                  Enterprise fraud analytics
                  pipelines remain stable
                  under live production monitoring.

                </p>

              </div>

            </div>

          </div>



          {/* ANALYTICS TABLE */}

          <div className="bg-white rounded-3xl shadow-lg p-8">

            <div className="flex items-center justify-between mb-8">

              <h2 className="text-3xl font-bold">

                Fraud Trend Analysis

              </h2>

              <div className="text-green-500 font-bold">

                ● UPDATED

              </div>

            </div>


            <div className="overflow-x-auto">

              <table className="w-full">

                <thead>

                  <tr className="border-b">

                    <th className="text-left py-4">

                      Category

                    </th>

                    <th className="text-left py-4">

                      Transactions

                    </th>

                    <th className="text-left py-4">

                      Risk Level

                    </th>

                    <th className="text-left py-4">

                      AI Confidence

                    </th>

                  </tr>

                </thead>


                <tbody>

                  <tr className="border-b">

                    <td className="py-5">

                      Card Fraud

                    </td>

                    <td>

                      240

                    </td>

                    <td className="text-red-500 font-bold">

                      HIGH

                    </td>

                    <td>

                      98%

                    </td>

                  </tr>


                  <tr className="border-b">

                    <td className="py-5">

                      Account Takeover

                    </td>

                    <td>

                      120

                    </td>

                    <td className="text-orange-500 font-bold">

                      MEDIUM

                    </td>

                    <td>

                      94%

                    </td>

                  </tr>


                  <tr className="border-b">

                    <td className="py-5">

                      Suspicious Transfers

                    </td>

                    <td>

                      86

                    </td>

                    <td className="text-red-500 font-bold">

                      HIGH

                    </td>

                    <td>

                      97%

                    </td>

                  </tr>


                  <tr>

                    <td className="py-5">

                      Behavioral Anomalies

                    </td>

                    <td>

                      65

                    </td>

                    <td className="text-blue-500 font-bold">

                      LOW

                    </td>

                    <td>

                      89%

                    </td>

                  </tr>

                </tbody>

              </table>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default FraudAnalytics;
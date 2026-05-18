import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

function MLMonitoring() {

  return (

    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-6 lg:p-8 max-w-[1600px] mx-auto">

          {/* PAGE TITLE */}

          <div className="mb-10">

            <h1 className="text-5xl font-extrabold text-gray-800 mb-4">

              ML Monitoring Center

            </h1>

            <p className="text-gray-600 text-lg">

              Real-time monitoring of machine learning
              fraud detection models and AI scoring systems.

            </p>

          </div>



          {/* TOP METRICS */}

          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">

            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                Model Accuracy

              </div>

              <div className="text-5xl font-bold text-green-600">

                98.2%

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                Fraud Precision

              </div>

              <div className="text-5xl font-bold text-blue-600">

                96.7%

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                False Positives

              </div>

              <div className="text-5xl font-bold text-orange-500">

                1.4%

              </div>

            </div>



            {/* CARD */}

            <div className="bg-white rounded-3xl p-6 shadow-lg">

              <div className="text-gray-500 mb-3">

                AI Status

              </div>

              <div className="text-4xl font-bold text-green-600">

                ACTIVE

              </div>

            </div>

          </div>



          {/* MODEL STATUS */}

          <div className="bg-white rounded-3xl shadow-lg p-8 mb-10">

            <div className="flex items-center justify-between mb-6">

              <h2 className="text-3xl font-bold">

                AI Model Status

              </h2>

              <div className="text-green-500 font-bold">

                ● RUNNING

              </div>

            </div>

            <p className="text-gray-600 leading-8 text-lg">

              FinRisk AI continuously evaluates
              financial transaction patterns using
              supervised machine learning models,
              anomaly detection pipelines,
              fraud classification engines,
              and risk intelligence systems.

            </p>

          </div>



          {/* MODEL PIPELINES */}

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

            {/* PIPELINE 1 */}

            <div className="bg-white rounded-3xl shadow-lg p-8">

              <h3 className="text-2xl font-bold mb-6">

                Fraud Detection Pipeline

              </h3>

              <div className="space-y-5">

                <div className="flex justify-between">

                  <span>Transaction Scoring</span>

                  <span className="text-green-600 font-bold">

                    ACTIVE

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>Risk Classification</span>

                  <span className="text-green-600 font-bold">

                    ACTIVE

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>Anomaly Detection</span>

                  <span className="text-green-600 font-bold">

                    ACTIVE

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>Real-Time Inference</span>

                  <span className="text-green-600 font-bold">

                    ACTIVE

                  </span>

                </div>

              </div>

            </div>



            {/* PIPELINE 2 */}

            <div className="bg-white rounded-3xl shadow-lg p-8">

              <h3 className="text-2xl font-bold mb-6">

                ML Infrastructure

              </h3>

              <div className="space-y-5">

                <div className="flex justify-between">

                  <span>Feature Engineering</span>

                  <span className="text-blue-600 font-bold">

                    READY

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>Model Registry</span>

                  <span className="text-blue-600 font-bold">

                    READY

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>ETL Pipelines</span>

                  <span className="text-blue-600 font-bold">

                    READY

                  </span>

                </div>

                <div className="flex justify-between">

                  <span>Prediction Engine</span>

                  <span className="text-blue-600 font-bold">

                    READY

                  </span>

                </div>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default MLMonitoring;
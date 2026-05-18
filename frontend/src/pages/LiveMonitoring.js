import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

import LiveTransactions from "../components/LiveTransactions";

import {
  fetchRecentTransactions
} from "../services/dashboardService";


function LiveMonitoring() {

  const [transactions,
    setTransactions] = useState([]);

  const [loading,
    setLoading] = useState(true);


  const token = localStorage.getItem("token");

  useEffect(() => {

    const loadTransactions =
      async () => {

      try {

        const txData =
          await fetchRecentTransactions(token);

        if (Array.isArray(txData)) {

          setTransactions(txData);

        } else if (
          txData.transactions
        ) {

          setTransactions(
            txData.transactions
          );
        }

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);
      }
    };

    loadTransactions();

  }, [token]);


  if (loading) {

    return (

      <div className="p-10 text-3xl">

        Loading Transactions...

      </div>
    );
  }


  return (

    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-8">

          <h1 className="text-4xl font-bold mb-8">

            Live Fraud Monitoring

          </h1>

          <LiveTransactions
            transactions={transactions}
          />

        </div>

      </div>

    </div>
  );
}

export default LiveMonitoring;
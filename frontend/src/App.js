import {

  BrowserRouter,

  Routes,

  Route

} from "react-router-dom";


import Dashboard from "./pages/Dashboard";

import FraudAnalytics from "./pages/FraudAnalytics";

import MLMonitoring from "./pages/MLMonitoring";

import ExplainableAI from "./pages/ExplainableAI";

import ProjectOverview from "./pages/ProjectOverview";

import LiveMonitoring from "./pages/LiveMonitoring";

import LandingPage from "./pages/LandingPage";


function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<LandingPage />} />

        <Route
  path="/dashboard"
  element={<Dashboard />}
/>

        <Route

          path="/fraud-analytics"

          element={<FraudAnalytics />}
        />

        <Route

          path="/ml-monitoring"

          element={<MLMonitoring />}
        />

        <Route

          path="/explainable-ai"

          element={<ExplainableAI />}
        />

        <Route

          path="/project-overview"

          element={<ProjectOverview />}
        />

        <Route

          path="/live-monitoring"

          element={<LiveMonitoring />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
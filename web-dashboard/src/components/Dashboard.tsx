import { useState, useEffect } from "react";
import {
  Activity,
  Zap,
  Clock,
  AlertTriangle,
  Gauge,
  Navigation,
  Droplets,
  Disc3,
  Users,
  DoorOpen,
  Fuel,
  Battery,
  Shield,
  Compass,
  Mountain,
  Thermometer,
  Move3D,
} from "lucide-react";

interface WarningLightProps {
  isOn: boolean;
  label: string;
  icon: React.ElementType;
  isGood?: boolean;
}
const WarningLight = ({ isOn, label, icon: Icon, isGood = false }: WarningLightProps) => (
  <div
    className={`flex items-center gap-1 px-2 py-1 rounded text-xs transition-all ${
      isOn
        ? isGood
          ? "bg-green-500/30 text-green-400 shadow-sm shadow-green-500/20"
          : "bg-red-500/30 text-red-400 shadow-sm shadow-red-500/20"
        : "text-gray-600"
    }`}
  >
    <Icon size={12} />
    <span className="font-medium">{label}</span>
  </div>
);

const AutomotiveDashboard = () => {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [gaugeData, setGaugeData] = useState({
    gauge1: 45,
    gauge2: 8,
    gauge3: 14.7,
    gauge4: 185,
    gauge5: 55,
  });

  const [electricalData, setElectricalData] = useState({
    voltage: 13.8,
    current: 24.5,
  });

  const [gpsData, setGpsData] = useState({
    speed: 45,
    heading: 142,
    altitude: 1250,
    gForce: 0.2,
    ambientTemp: 72,
  });

  const [warningLights, setWarningLights] = useState({
    cruise: true,
    checkEngine: false,
    lowCoolant: false,
    oilPressure: false,
    brake: false,
    seatBelt: false,
    doorAjar: false,
    lowFuel: false,
    chargingFault: false,
    security: false,
  });

  // Simulate real-time data updates
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());

      setGaugeData((prev) => ({
        gauge1: Math.max(
          10,
          Math.min(80, prev.gauge1 + (Math.random() - 0.5) * 3)
        ),
        gauge2: Math.max(
          -5,
          Math.min(25, prev.gauge2 + (Math.random() - 0.5) * 2)
        ),
        gauge3: Math.max(
          10.0,
          Math.min(18.0, prev.gauge3 + (Math.random() - 0.5) * 0.5)
        ),
        gauge4: Math.max(
          160,
          Math.min(220, prev.gauge4 + (Math.random() - 0.5) * 3)
        ),
        gauge5: Math.max(
          0,
          Math.min(100, prev.gauge5 + (Math.random() - 0.5) * 3)
        ),
      }));

      setElectricalData((prev) => ({
        voltage: Math.max(
          11.5,
          Math.min(14.5, prev.voltage + (Math.random() - 0.5) * 0.2)
        ),
        current: Math.max(
          0,
          Math.min(50, prev.current + (Math.random() - 0.5) * 2)
        ),
      }));

      setGpsData((prev) => ({
        speed: Math.max(
          0,
          Math.min(80, prev.speed + (Math.random() - 0.5) * 5)
        ),
        heading: (prev.heading + (Math.random() - 0.5) * 10 + 360) % 360,
        altitude: Math.max(
          800,
          Math.min(2000, prev.altitude + (Math.random() - 0.5) * 20)
        ),
        gForce: Math.max(
          -1.5,
          Math.min(1.5, prev.gForce + (Math.random() - 0.5) * 0.3)
        ),
        ambientTemp: Math.max(
          32,
          Math.min(110, prev.ambientTemp + (Math.random() - 0.5) * 2)
        ),
      }));

      if (Math.random() < 0.05) {
        setWarningLights((prev) => ({
          ...prev,
          checkEngine: Math.random() < 0.1,
          oilPressure: Math.random() < 0.05,
          seatBelt: Math.random() < 0.3,
          lowFuel: Math.random() < 0.15,
          doorAjar: Math.random() < 0.2,
        }));
      }
    }, 500);

    return () => clearInterval(interval);
  }, []);

  interface CompactGaugeProps {
    value: number;
    label: string;
    unit: string;
    color?: string;
    max?: number;
  }
  const CompactGauge = ({ value, label, unit, color = "blue", max = 100 }: CompactGaugeProps) => {
    const percentage = (value / max) * 100;
    const circumference = 2 * Math.PI * 35;
    const strokeDasharray = circumference;
    const strokeDashoffset = circumference - (percentage / 100) * circumference;

    return (
      <div className="flex flex-col items-center bg-gray-900/80 p-3 rounded-xl backdrop-blur-sm border border-gray-700/50">
        <div className="relative w-20 h-20 mb-1">
          <svg className="w-20 h-20 transform -rotate-90" viewBox="0 0 80 80">
            <defs>
              <linearGradient
                id={`gradient-${color}`}
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
              >
                <stop
                  offset="0%"
                  stopColor={
                    color === "blue"
                      ? "#3b82f6"
                      : color === "green"
                      ? "#10b981"
                      : color === "yellow"
                      ? "#f59e0b"
                      : color === "red"
                      ? "#ef4444"
                      : "#8b5cf6"
                  }
                />
                <stop
                  offset="100%"
                  stopColor={
                    color === "blue"
                      ? "#1d4ed8"
                      : color === "green"
                      ? "#047857"
                      : color === "yellow"
                      ? "#d97706"
                      : color === "red"
                      ? "#dc2626"
                      : "#7c3aed"
                  }
                />
              </linearGradient>
            </defs>
            <circle
              cx="40"
              cy="40"
              r="35"
              stroke="rgb(55, 65, 81)"
              strokeWidth="6"
              fill="none"
              opacity="0.3"
            />
            <circle
              cx="40"
              cy="40"
              r="35"
              stroke={`url(#gradient-${color})`}
              strokeWidth="6"
              fill="none"
              strokeDasharray={strokeDasharray}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              className="transition-all duration-700 ease-out"
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-lg font-bold text-white">
              {value < 20 ? value.toFixed(1) : Math.round(value)}
            </span>
            <span className="text-xs text-gray-400">{unit}</span>
          </div>
        </div>
        <span className="text-xs font-medium text-gray-300">{label}</span>
      </div>
    );
  };

  const getCompassDirection = (heading: number) => {
    const directions = [
      "N",
      "NNE",
      "NE",
      "ENE",
      "E",
      "ESE",
      "SE",
      "SSE",
      "S",
      "SSW",
      "SW",
      "WSW",
      "W",
      "WNW",
      "NW",
      "NNW",
    ];
    const index = Math.round(heading / 22.5) % 16;
    return directions[index];
  };

  interface MiniDataCardProps {
    label: string;
    value: string | number;
    unit?: string;
    color?: string;
    icon: React.ElementType;
  }
  const MiniDataCard = ({ label, value, unit, color, icon: Icon }: MiniDataCardProps) => (
    <div className="bg-gray-800/60 rounded-md p-1.5 flex items-center gap-1.5">
      <Icon size={14} className={color} />
      <div className="flex flex-col">
        <span className="text-xs text-gray-400">{label}</span>
        <span className={`text-sm font-mono font-bold ${color}`}>
          {value}
          {unit}
        </span>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 text-white p-2">
      {/* Compact Header */}
      <div className="flex justify-between items-center mb-3 bg-gray-900/50 backdrop-blur-sm rounded-lg p-2">
        <div className="flex items-center gap-2">
          <Gauge className="text-blue-400" size={20} />
          <h1 className="text-lg font-bold">Vehicle Telemetry</h1>
        </div>
        <div className="flex items-center gap-3 text-sm">
          <div className="flex items-center gap-1">
            <Clock size={14} />
            <span className="font-mono">
              {currentTime.toLocaleTimeString()}
            </span>
          </div>
          <div className="flex items-center gap-1 text-green-400">
            <Activity size={14} />
            <span>ONLINE</span>
          </div>
        </div>
      </div>

      {/* Main Content - Single Row Layout */}
      <div className="grid grid-cols-12 gap-3 mb-3">
        {/* 5 Gauges - Takes up 8 columns */}
        <div className="col-span-8">
          <div className="bg-gray-900/50 backdrop-blur-sm rounded-lg p-3">
            <div className="grid grid-cols-5 gap-2">
              <CompactGauge
                value={gaugeData.gauge1}
                label="Oil Press"
                unit="PSI"
                color="blue"
                max={100}
              />
              <CompactGauge
                value={gaugeData.gauge2}
                label="Boost"
                unit="PSI"
                color="green"
                max={30}
              />
              <CompactGauge
                value={gaugeData.gauge3}
                label="AFR"
                unit="A/F"
                color="yellow"
                max={18}
              />
              <CompactGauge
                value={gaugeData.gauge4}
                label="Water Temp"
                unit="°F"
                color="red"
                max={250}
              />
              <CompactGauge
                value={gaugeData.gauge5}
                label="Fuel Press"
                unit="PSI"
                color="purple"
                max={100}
              />
            </div>
          </div>
        </div>

        {/* Side Panel - Takes up 4 columns */}
        <div className="col-span-4 space-y-2">
          {/* Speed Display - Prominent */}
          <div className="bg-gray-900/50 backdrop-blur-sm rounded-lg p-3">
            <div className="text-center">
              <div className="text-3xl font-bold text-green-400 font-mono">
                {Math.round(gpsData.speed)}
              </div>
              <div className="text-sm text-gray-400">MPH</div>
            </div>
          </div>

          {/* Electrical Data */}
          <div className="bg-gray-900/50 backdrop-blur-sm rounded-lg p-2">
            <div className="grid grid-cols-2 gap-1">
              <MiniDataCard
                label="Volts"
                value={electricalData.voltage.toFixed(1)}
                unit="V"
                color="text-yellow-400"
                icon={Zap}
              />
              <MiniDataCard
                label="Amps"
                value={electricalData.current.toFixed(0)}
                unit="A"
                color="text-blue-400"
                icon={Activity}
              />
            </div>
          </div>

          {/* IMU & GPS Data */}
          <div className="bg-gray-900/50 backdrop-blur-sm rounded-lg p-2">
            <div className="grid grid-cols-2 gap-1">
              <MiniDataCard
                label="Heading"
                value={`${Math.round(gpsData.heading)}° ${getCompassDirection(
                  gpsData.heading
                )}`}
                unit=""
                color="text-purple-400"
                icon={Compass}
              />
              <MiniDataCard
                label="Altitude"
                value={Math.round(gpsData.altitude)}
                unit="ft"
                color="text-cyan-400"
                icon={Mountain}
              />
              <MiniDataCard
                label="G-Force"
                value={
                  gpsData.gForce >= 0
                    ? `+${gpsData.gForce.toFixed(1)}`
                    : gpsData.gForce.toFixed(1)
                }
                unit="g"
                color={
                  Math.abs(gpsData.gForce) > 0.8
                    ? "text-red-400"
                    : "text-green-400"
                }
                icon={Move3D}
              />
              <MiniDataCard
                label="Ambient"
                value={Math.round(gpsData.ambientTemp)}
                unit="°F"
                color="text-orange-400"
                icon={Thermometer}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Warning Lights - Bottom Strip */}
      <div className="bg-gray-900/50 backdrop-blur-sm rounded-lg p-2">
        <div className="grid grid-cols-5 gap-2">
          <WarningLight
            isOn={warningLights.cruise}
            label="CRUISE"
            icon={Navigation}
            isGood={true}
          />
          <WarningLight
            isOn={warningLights.checkEngine}
            label="CEL"
            icon={AlertTriangle}
          />
          <WarningLight
            isOn={warningLights.lowCoolant}
            label="COOLANT"
            icon={Droplets}
          />
          <WarningLight
            isOn={warningLights.oilPressure}
            label="OIL"
            icon={AlertTriangle}
          />
          <WarningLight isOn={warningLights.brake} label="BRAKE" icon={Disc3} />
          <WarningLight
            isOn={warningLights.seatBelt}
            label="BELT"
            icon={Users}
          />
          <WarningLight
            isOn={warningLights.doorAjar}
            label="DOOR"
            icon={DoorOpen}
          />
          <WarningLight isOn={warningLights.lowFuel} label="FUEL" icon={Fuel} />
          <WarningLight
            isOn={warningLights.chargingFault}
            label="CHARGE"
            icon={Battery}
          />
          <WarningLight
            isOn={warningLights.security}
            label="SECURITY"
            icon={Shield}
          />
        </div>
      </div>
    </div>
  );
};

export default AutomotiveDashboard;

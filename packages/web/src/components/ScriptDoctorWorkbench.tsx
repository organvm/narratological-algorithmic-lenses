import React, { useState, useEffect } from 'react';
import { api } from '../api/client';

interface StudySummary {
  id: string;
  creator: string;
  category: string;
}

interface ScriptDoctorPair {
  theme: string;
  primary_id: string;
  secondary_id: string;
}

interface DebateRound {
  round: string;
  content: string;
}

interface DialogueEntry {
  creator: string;
  feedback: string;
}

interface ScriptDoctorResult {
  pair: ScriptDoctorPair;
  debate_rounds?: DebateRound[];
  dialogue: DialogueEntry[];
  joint_recommendations: string[];
  creative_tension: string[];
  final_prescription: string;
}

export const ScriptDoctorWorkbench: React.FC = () => {
  const [content, setContent] = useState('');
  const [studies, setStudies] = useState<StudySummary[]>([]);
  const [primaryId, setPrimaryId] = useState('');
  const [secondaryId, setSecondaryId] = useState('');
  const [debateMode, setDebateMode] = useState(false);
  const [result, setResult] = useState<ScriptDoctorResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStudies = async () => {
      try {
        const data = await api.get<StudySummary[]>('/analysis/frameworks');
        setStudies(data);
        if (data.length >= 2) {
          setPrimaryId(data[0].id);
          setSecondaryId(data[1].id);
        }
      } catch (err) {
        console.error('Failed to fetch studies', err);
      }
    };
    fetchStudies();
  }, []);

  const handleConsult = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await api.post<ScriptDoctorResult>('/analysis/script-doctor', {
        content,
        primary_id: primaryId,
        secondary_id: secondaryId,
        debate_mode: debateMode,
      });
      setResult(response);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : 'Analysis failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="script-doctor-workbench p-6 max-w-6xl mx-auto">
      <header className="mb-8 border-b pb-4">
        <h1 className="text-3xl font-bold text-magenta-600">The Script Doctor Workbench</h1>
        <p className="text-gray-600">Simulate a dialectical consultation between master creators.</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section className="input-section flex flex-col gap-4">
          <div className="controls bg-gray-50 p-4 rounded-lg border flex flex-col gap-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-semibold mb-1">Primary Doctor</label>
                <select 
                  className="w-full p-2 border rounded"
                  value={primaryId}
                  onChange={(e) => setPrimaryId(e.target.value)}
                >
                  {studies.map(s => (
                    <option key={s.id} value={s.id}>{s.creator}</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-sm font-semibold mb-1">Secondary Doctor</label>
                <select 
                  className="w-full p-2 border rounded"
                  value={secondaryId}
                  onChange={(e) => setSecondaryId(e.target.value)}
                >
                  {studies.map(s => (
                    <option key={s.id} value={s.id}>{s.creator}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <input 
                type="checkbox" 
                id="debate-toggle"
                checked={debateMode}
                onChange={(e) => setDebateMode(e.target.checked)}
              />
              <label htmlFor="debate-toggle" className="text-sm font-medium">Enable Multi-Agent Debate Mode</label>
            </div>

            <button 
              onClick={handleConsult}
              disabled={loading || !content}
              className={`w-full py-3 rounded-lg font-bold text-white transition-all ${
                loading || !content ? 'bg-gray-400' : 'bg-magenta-600 hover:bg-magenta-700 shadow-lg'
              }`}
            >
              {loading ? 'Consulting the Doctors...' : 'Start Consultation'}
            </button>
          </div>

          <textarea 
            className="w-full h-96 p-4 font-mono text-sm border rounded-lg focus:ring-2 focus:ring-magenta-500 outline-none"
            placeholder="Paste your Fountain or text script here..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
        </section>

        <section className="output-section bg-white border rounded-lg shadow-inner min-h-[500px] p-6 overflow-y-auto">
          {error && (
            <div className="bg-red-50 text-red-700 p-4 rounded border border-red-200 mb-4">
              {error}
            </div>
          )}

          {!result && !loading && (
            <div className="flex flex-col items-center justify-center h-full text-gray-400 italic">
              Enter your script and select the doctors to begin the synthesis.
            </div>
          )}

          {loading && (
            <div className="flex flex-col items-center justify-center h-full space-y-4">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-magenta-600"></div>
              <p className="text-magenta-600 font-medium animate-pulse">Orchestrating Philosophical Friction...</p>
            </div>
          )}

          {result && (
            <div className="result-display space-y-8 animate-in fade-in duration-500">
              <div className="result-header bg-magenta-50 p-4 rounded border-l-4 border-magenta-500">
                <h2 className="text-lg font-bold text-magenta-900">Theme: {result.pair.theme}</h2>
                <p className="text-sm text-magenta-700">Pairing: {result.pair.primary_id} & {result.pair.secondary_id}</p>
              </div>

              {result.debate_rounds && (
                <div className="debate-rounds space-y-4">
                  <h3 className="text-md font-bold uppercase tracking-wider text-gray-500 border-b pb-1">Dialectical Rounds</h3>
                  {result.debate_rounds.map((round, i) => (
                    <div key={i} className="round bg-yellow-50 p-4 rounded border border-yellow-100 shadow-sm">
                      <h4 className="font-bold text-yellow-900 mb-2">{round.round}</h4>
                      <p className="text-sm text-yellow-800 leading-relaxed whitespace-pre-wrap">{round.content}</p>
                    </div>
                  ))}
                </div>
              )}

              <div className="collaborative-dialogue space-y-4">
                <h3 className="text-md font-bold uppercase tracking-wider text-gray-500 border-b pb-1">Joint Consultation</h3>
                {result.dialogue.map((entry, i) => (
                  <div key={i} className={`dialogue-entry p-4 rounded-lg ${i % 2 === 0 ? 'bg-blue-50 ml-4' : 'bg-green-50 mr-4'}`}>
                    <span className="block font-bold text-xs uppercase mb-1 opacity-60">{entry.creator}</span>
                    <p className="text-sm italic text-gray-800">{entry.feedback}</p>
                  </div>
                ))}
              </div>

              <div className="recommendations grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="joint-rec p-4 bg-gray-50 rounded border">
                  <h4 className="font-bold text-green-800 mb-2">Prescription</h4>
                  <ul className="text-xs space-y-2 list-disc pl-4">
                    {result.joint_recommendations.map((r: string, i: number) => (
                      <li key={i}>{r}</li>
                    ))}
                  </ul>
                </div>
                <div className="creative-tension p-4 bg-gray-50 rounded border">
                  <h4 className="font-bold text-orange-800 mb-2">Creative Tension</h4>
                  <ul className="text-xs space-y-2 list-disc pl-4">
                    {result.creative_tension.map((t: string, i: number) => (
                      <li key={i}>{t}</li>
                    ))}
                  </ul>
                </div>
              </div>

              <div className="final-prescription bg-black p-6 rounded-lg text-center shadow-xl">
                <h3 className="text-magenta-400 font-bold uppercase text-xs mb-2">Final Doctor's Orders</h3>
                <p className="text-white font-serif text-lg italic">{result.final_prescription}</p>
              </div>
            </div>
          )}
        </section>
      </div>
    </div>
  );
};

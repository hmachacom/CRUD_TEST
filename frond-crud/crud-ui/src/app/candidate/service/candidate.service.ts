import { Injectable } from '@angular/core';
import { environment } from '../../../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { ICandidate } from '../models/candidate';

@Injectable({
  providedIn: 'root',
})
export class CandidateService {
  private api = environment.apiUrl;

  constructor(private http: HttpClient) {}
  getCandidate(id: number) {
    return this.http.get<ICandidate>(`${this.api}/candidates/${id}`);
  }
  getCandidates() {
    return this.http.get<ICandidate[]>(`${this.api}/candidates`);
  }
  deleteCandidate(id: number) {
    return this.http.delete(`${this.api}/candidates/${id}`);
  }
  createCandidate(candidate: Partial<ICandidate>) {
    return this.http.post(`${this.api}/candidates`, candidate);
  }
}

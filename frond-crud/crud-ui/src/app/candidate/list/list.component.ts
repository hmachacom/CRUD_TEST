import { Component, OnInit } from '@angular/core';
import { CandidateService } from '../service/candidate.service';
import { ICandidate } from '../models/candidate';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrl: './list.component.css',
})
export class ListComponent implements OnInit {
  constructor(private candidateService: CandidateService) {}

  candidates: ICandidate[] = [];

  ngOnInit(): void {
    this.getCandidates();
  }

  getCandidates() {
    this.candidateService.getCandidates().subscribe(
      (data) => {
        this.candidates = data;
        console.log(data);
      },
      (error) => {
        console.log(error);
      }
    );
  }
  addCandidate() {}
  deleteCandidate(candidate: any) {}
  editCandidate(candidate: any) {}
}
